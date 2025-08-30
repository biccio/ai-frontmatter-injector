import os
import json
import yaml
import google.generativeai as genai
from pathlib import Path
from supabase import create_client, Client

# --- Funzioni di Caricamento Risorse ---

def load_prompt_and_knowledge_base() -> tuple[str, str]:
    """
    Carica il prompt master e la knowledge base testuale (escludendo schema.org).
    """
    try:
        script_dir = Path(__file__).resolve().parent
        prompt_path = script_dir / "config" / "master_prompt.txt"
        
        with open(prompt_path, "r", encoding="utf-8") as f:
            prompt_template = f.read()
        
        knowledge_base_content = ""
        kb_path = script_dir / "knowledge_base"
        if kb_path.is_dir():
            for file_path in kb_path.glob('*.*'):
                if 'schemaorg' not in file_path.name:
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        knowledge_base_content += f.read() + "\n\n"

        return prompt_template, knowledge_base_content.strip()
    except FileNotFoundError as e:
        raise SystemExit(f"Errore: File di configurazione non trovato. Controlla che il percorso sia corretto.\nDettagli: {e}")

def load_product_info() -> dict:
    """Carica le informazioni sul prodotto dal file JSON di configurazione."""
    script_dir = Path(__file__).resolve().parent
    product_info_path = script_dir / "config" / "product_info.json"
    if not product_info_path.exists():
        return {"nome": "N/A", "versione": "N/A"}
    try:
        with open(product_info_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return {"nome": "N/A", "versione": "N/A"}


# --- Funzioni di Configurazione AI ---
def configure_ai_models() -> tuple[genai.GenerativeModel, str, Client]:
    """Configura e restituisce il modello generativo, il modello di embedding e il client Supabase."""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise SystemExit("Errore: La chiave API 'GEMINI_API_KEY' non è stata trovata.")
    genai.configure(api_key=api_key)
    
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY")
    if not url or not key:
        raise SystemExit("Errore: Credenziali Supabase non trovate.")
    supabase = create_client(url, key)
    
    generative_model = genai.GenerativeModel('gemini-1.5-pro')
    embedding_model_name = 'models/embedding-001'
    
    return generative_model, embedding_model_name, supabase

# --- Funzione di Ricerca Vettoriale ---
def retrieve_relevant_schemas(supabase: Client, embedding_model: str, query_text: str) -> str:
    """
    Genera un embedding per il testo di query e recupera gli schemi pertinenti da Supabase.
    """
    if not query_text:
        return "Nessun contenuto da analizzare."

    try:
        query_embedding_result = genai.embed_content(
            model=embedding_model,
            content=query_text,
            task_type="RETRIEVAL_QUERY"
        )
        query_embedding = query_embedding_result['embedding']

        response = supabase.rpc('match_schemas', {
            'query_embedding': query_embedding,
            'match_threshold': 0.75, 
            'match_count': 3 
        }).execute()
        
        relevant_docs = [item['content'] for item in response.data]
        return "\n".join(relevant_docs) if relevant_docs else "Nessuno schema pertinente trovato."
        
    except Exception as e:
        print(f"  -> Errore durante la ricerca su Supabase: {e}")
        return "Errore durante il recupero degli schemi."

# --- Funzione di Generazione ---
def generate_frontmatter(model, prompt_template: str, schema_context: str, kb_content: str, content: str, product_info: dict) -> str | None:
    """
    Genera il frontmatter chiamando l'API, usando il contesto e le info sul prodotto.
    """
    final_prompt = prompt_template.replace("{{KNOWLEDGE_BASE_CONTENT}}", kb_content)
    final_prompt = final_prompt.replace("{{SCHEMA_DEFINITIONS}}", schema_context)
    final_prompt = final_prompt.replace("{{MARKDOWN_CONTENT}}", content)
    final_prompt = final_prompt.replace("{{PRODUCT_NAME}}", product_info.get("nome", "N/A"))
    final_prompt = final_prompt.replace("{{PRODUCT_VERSION}}", product_info.get("versione", "N/A"))
    
    try:
        generation_config = genai.types.GenerationConfig(response_mime_type="text/plain")
        response = model.generate_content(final_prompt, generation_config=generation_config)
        cleaned_response = response.text.strip().removeprefix("```yaml").removeprefix("```").removesuffix("```").strip()
        return cleaned_response
    except Exception as e:
        print(f"  -> Errore durante la chiamata all'API AI: {e}")
        return None

# --- Funzione di Validazione ---
def validate_and_parse_yaml(yaml_string: str) -> dict | None:
    """Tenta di fare il parsing di una stringa YAML e la restituisce come dizionario."""
    try:
        data = yaml.safe_load(yaml_string)
        if isinstance(data, dict):
            return data
        else:
            # print("--- INIZIO OUTPUT AI NON VALIDO (Tipo non dizionario) ---")
            # print(yaml_string)
            # print("--- FINE OUTPUT AI NON VALIDO ---")
            return None
    except yaml.YAMLError as e:
        # print("--- INIZIO OUTPUT AI NON VALIDO (Errore di parsing) ---")
        # print(yaml_string)
        # print(f"Dettagli errore parser YAML: {e}")
        # print("--- FINE OUTPUT AI NON VALIDO ---")
        return None

