import os
import json
from dotenv import load_dotenv
from supabase import create_client, Client
import google.generativeai as genai
from pathlib import Path
import rdflib
from rdflib.namespace import RDFS, RDF

# Configura il modello di embedding
def configure_embedding_model():
    """Configura e restituisce il modello di embedding di Gemini."""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise SystemExit("Errore: GEMINI_API_KEY non trovata in .env")
    genai.configure(api_key=api_key)
    return 'models/embedding-001' # Modello di embedding consigliato

def parse_schema_org_rdf(file_path: Path) -> dict:
    """
    Legge un file RDF di schema.org, lo analizza e lo trasforma
    in un dizionario Python più semplice da usare.
    """
    print(f"Lettura e parsing del file RDF: {file_path}...")
    
    # Rileva il formato corretto dall'estensione del file
    file_extension = file_path.suffix.lower()
    rdf_format = ''
    if file_extension == '.jsonld':
        rdf_format = 'json-ld'
    elif file_extension == '.rdf':
        rdf_format = 'xml'  # Il formato .rdf di schema.org è solitamente RDF/XML
    else:
        raise SystemExit(f"Errore: estensione file non supportata '{file_extension}'. Usare .jsonld o .rdf.")
    
    print(f"Formato RDF rilevato: '{rdf_format}'")

    g = rdflib.Graph()
    g.parse(str(file_path), format=rdf_format)
    print("Parsing completato. Estrazione degli schemi...")

    schemas = {}
    
    # Query SPARQL per trovare tutte le Classi e la loro descrizione (commento)
    query_classes = """
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX schema: <https://schema.org/>
        SELECT ?class ?comment
        WHERE {
            ?class a rdfs:Class .
            ?class rdfs:comment ?comment .
            FILTER(STRSTARTS(STR(?class), "https://schema.org/"))
        }
    """

    for row in g.query(query_classes):
        # CORREZIONE: Usa la notazione a dizionario per evitare conflitti con la parola chiave 'class'
        class_uri = str(row["class"])
        class_name = class_uri.replace("https://schema.org/", "")
        
        # Ignoriamo tipi di dati (es. Text, Number) che non sono veri schemi
        if class_name[0].islower():
            continue
            
        schemas[class_name] = {
            "description": str(row["comment"]),
            "properties": {} # Verrà popolato dopo
        }

    # Query SPARQL per trovare tutte le Proprietà
    query_properties = """
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX schema: <https://schema.org/>
        SELECT ?prop ?comment ?domain
        WHERE {
            ?prop a rdf:Property .
            ?prop rdfs:comment ?comment .
            ?prop schema:domainIncludes ?domain .
            FILTER(STRSTARTS(STR(?prop), "https://schema.org/"))
        }
    """
    
    for row in g.query(query_properties):
        # CORREZIONE: Usa la notazione a dizionario per coerenza e robustezza
        prop_name = str(row["prop"]).replace("https://schema.org/", "")
        domain_name = str(row["domain"]).replace("https://schema.org/", "")
        
        if domain_name in schemas:
            schemas[domain_name]["properties"][prop_name] = str(row["comment"])

    print(f"Estratti {len(schemas)} schemi validi dal file RDF.")
    return schemas


def main():
    """
    Script per leggere la knowledge base, generare embeddings e caricarli su Supabase.
    """
    load_dotenv()

    # 1. Connessione a Supabase
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")
    if not url or not key:
        raise SystemExit("Errore: SUPABASE_URL o SUPABASE_KEY non trovate in .env")
    
    supabase: Client = create_client(url, key)
    print("Connesso a Supabase.")

    # 2. Configurazione del modello AI per gli embeddings
    embedding_model = configure_embedding_model()
    print(f"Modello di embedding '{embedding_model}' configurato.")

    # 3. Lettura e parsing del file RDF di schema.org
    kb_path = Path("knowledge_base")
    # Cerca un file che contenga 'schemaorg' con estensioni .jsonld o .rdf
    schema_file = None
    for ext in ['.jsonld', '.rdf']:
        file = next(kb_path.glob(f'*schemaorg*{ext}'), None)
        if file:
            schema_file = file
            break
            
    if not schema_file:
        raise SystemExit("Errore: Nessun file schema.org ('*.jsonld' o '*.rdf') trovato in knowledge_base/")

    schema_data = parse_schema_org_rdf(schema_file)

    if not schema_data:
        raise SystemExit("Errore: Nessuno schema è stato estratto dal file RDF.")

    print(f"Inizio l'indicizzazione di {len(schema_data)} schemi...")

    # 4. Generazione embeddings e caricamento
    for schema_name, schema_info in schema_data.items():
        # Prepara il testo da indicizzare
        description = schema_info.get("description", "")
        properties = ", ".join(schema_info.get("properties", {}).keys())
        content_to_embed = f"Schema: {schema_name}. Descrizione: {description}. Proprietà: {properties}."
        
        print(f"  - Generazione embedding per '{schema_name}'...")
        
        # Genera l'embedding
        embedding_result = genai.embed_content(
            model=embedding_model,
            content=content_to_embed,
            task_type="RETRIEVAL_DOCUMENT" # Importante per la ricerca
        )
        embedding = embedding_result['embedding']

        # Prepara il dato da inserire
        data_to_insert = {
            "schema_name": schema_name,
            "content": content_to_embed,
            "embedding": embedding
        }

        # Inserisce nel database
        try:
            supabase.table("schema_embeddings").insert(data_to_insert).execute()
            print(f"    -> '{schema_name}' indicizzato con successo.")
        except Exception as e:
            print(f"    -> Errore durante l'inserimento di '{schema_name}': {e}")

    print("\nIndicizzazione completata.")

if __name__ == "__main__":
    main()

