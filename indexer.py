from pathlib import Path

import chromadb
import rdflib
from dotenv import load_dotenv
from rdflib.namespace import RDFS, RDF

import ai_core

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
        # Ignoriamo anche stringhe vuote per evitare IndexError
        if not class_name or class_name[0].islower():
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
    Script per leggere la knowledge base, generare embeddings e indicizzarli su ChromaDB.
    """
    load_dotenv()

    print("Configurazione della funzione di embedding...")
    embedding_provider = ai_core.resolve_embedding_provider()
    embedding_function = ai_core.configure_embedding_function(embedding_provider)

    client = chromadb.PersistentClient(path=ai_core.get_chroma_persist_directory())
    collection = client.get_or_create_collection(
        name="schema_embeddings",
        embedding_function=embedding_function,
    )
    print(f"Collection 'schema_embeddings' pronta su ChromaDB (provider embedding: {embedding_provider}).")

    # Lettura e parsing del file RDF di schema.org
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

    # Generazione embeddings e caricamento
    for schema_name, schema_info in schema_data.items():
        # Prepara il testo da indicizzare
        description = schema_info.get("description", "")
        properties = ", ".join(schema_info.get("properties", {}).keys())
        content_to_embed = f"Schema: {schema_name}. Descrizione: {description}. Proprietà: {properties}."

        print(f"  - Indicizzazione di '{schema_name}'...")

        # Inserisce/aggiorna nel database vettoriale
        try:
            collection.upsert(
                ids=[schema_name],
                documents=[content_to_embed],
                metadatas=[{"schema_name": schema_name}],
            )
            print(f"    -> '{schema_name}' indicizzato con successo.")
        except Exception as e:
            print(f"    -> Errore durante l'inserimento di '{schema_name}': {e}")

    print("\nIndicizzazione completata.")

if __name__ == "__main__":
    main()

