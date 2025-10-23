import os
import json
import yaml
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import chromadb
import google.generativeai as genai
from anthropic import Anthropic
from chromadb.api.models.Collection import Collection
from chromadb.utils import embedding_functions
from openai import OpenAI

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


# --- Funzioni di Configurazione AI e Vector Store ---

@dataclass
class LLMConfig:
    provider: str
    client: Any
    model: str
    embedding_provider: str


def get_chroma_persist_directory() -> str:
    """Restituisce il percorso di persistenza per ChromaDB."""
    env_path = os.getenv("CHROMA_DB_PATH")
    if env_path:
        return str(Path(env_path).expanduser())
    return str(Path(__file__).resolve().parent / "chroma_db")


def resolve_embedding_provider() -> str:
    """Determina il provider degli embeddings basandosi sulla configurazione."""
    override = os.getenv("EMBEDDING_PROVIDER")
    if override:
        return override.strip().lower()

    llm_provider = (os.getenv("LLM_PROVIDER") or "gemini").strip().lower()
    if llm_provider == "openai":
        return "openai"
    return "google"


def configure_embedding_function(provider: str | None = None):
    """Configura la funzione di embedding da usare con ChromaDB."""
    provider_name = (provider or resolve_embedding_provider()).strip().lower()

    if provider_name in {"google", "gemini"}:
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise SystemExit("Errore: La chiave API 'GEMINI_API_KEY' è necessaria per gli embeddings di Google.")
        genai.configure(api_key=api_key)
        model_name = os.getenv("GEMINI_EMBEDDING_MODEL", "models/embedding-001")
        return embedding_functions.GoogleGenerativeAIEmbeddingFunction(api_key=api_key, model_name=model_name)

    if provider_name == "openai":
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise SystemExit("Errore: La chiave API 'OPENAI_API_KEY' è necessaria per gli embeddings di OpenAI.")
        model_name = os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-large")
        return embedding_functions.OpenAIEmbeddingFunction(api_key=api_key, model_name=model_name)

    if provider_name in {"sentence-transformers", "sentence_transformers", "local"}:
        model_name = os.getenv("SENTENCE_TRANSFORMER_MODEL", "all-MiniLM-L6-v2")
        return embedding_functions.SentenceTransformerEmbeddingFunction(model_name=model_name)

    raise SystemExit(f"Errore: Provider di embedding '{provider_name}' non supportato.")


def configure_ai_models() -> tuple[LLMConfig, Collection]:
    """Configura e restituisce il modello generativo selezionato e la collection ChromaDB."""

    provider = (os.getenv("LLM_PROVIDER") or "gemini").strip().lower()
    embedding_override = os.getenv("EMBEDDING_PROVIDER")
    model_name: str

    if provider == "gemini":
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise SystemExit("Errore: La chiave API 'GEMINI_API_KEY' non è stata trovata.")
        genai.configure(api_key=api_key)
        model_name = os.getenv("GEMINI_MODEL", "gemini-2.5-pro")
        client = genai.GenerativeModel(model_name)
        default_embedding = "google"

    elif provider == "openai":
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise SystemExit("Errore: La chiave API 'OPENAI_API_KEY' non è stata trovata.")
        model_name = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
        client = OpenAI(api_key=api_key)
        default_embedding = "openai"

    elif provider == "claude":
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise SystemExit("Errore: La chiave API 'ANTHROPIC_API_KEY' non è stata trovata.")
        model_name = os.getenv("CLAUDE_MODEL", "claude-3-5-sonnet-20240620")
        client = Anthropic(api_key=api_key)
        default_embedding = "google"

    else:
        raise SystemExit(f"Errore: Provider LLM '{provider}' non supportato. Usare 'gemini', 'openai' o 'claude'.")

    embedding_provider = (embedding_override or default_embedding).strip().lower()
    embedding_function = configure_embedding_function(embedding_provider)

    client = chromadb.PersistentClient(path=get_chroma_persist_directory())
    collection = client.get_or_create_collection(
        name="schema_embeddings",
        embedding_function=embedding_function,
    )

    llm_config = LLMConfig(provider=provider, client=client, model=model_name, embedding_provider=embedding_provider)

    return llm_config, collection


# --- Funzione di Ricerca Vettoriale ---
def retrieve_relevant_schemas(collection: Collection, query_text: str) -> str:
    """Esegue una ricerca vettoriale su ChromaDB per ottenere gli schemi più pertinenti."""
    if not query_text:
        return "Nessun contenuto da analizzare."

    try:
        results = collection.query(query_texts=[query_text], n_results=3)
        documents = results.get("documents", [])
        if documents and documents[0]:
            return "\n".join(documents[0])
        return "Nessuno schema pertinente trovato."
    except Exception as e:
        print(f"  -> Errore durante la ricerca su ChromaDB: {e}")
        return "Errore durante il recupero degli schemi."


# --- Funzione di Generazione ---
def generate_frontmatter(llm_config: LLMConfig, prompt_template: str, schema_context: str, kb_content: str, content: str, product_info: dict) -> str | None:
    """Genera il frontmatter usando il provider LLM selezionato."""
    final_prompt = prompt_template.replace("{{KNOWLEDGE_BASE_CONTENT}}", kb_content)
    final_prompt = final_prompt.replace("{{SCHEMA_DEFINITIONS}}", schema_context)
    final_prompt = final_prompt.replace("{{MARKDOWN_CONTENT}}", content)
    final_prompt = final_prompt.replace("{{PRODUCT_NAME}}", product_info.get("nome", "N/A"))
    final_prompt = final_prompt.replace("{{PRODUCT_VERSION}}", product_info.get("versione", "N/A"))

    try:
        if llm_config.provider == "gemini":
            generation_config = genai.types.GenerationConfig(response_mime_type="text/plain")
            response = llm_config.client.generate_content(final_prompt, generation_config=generation_config)
            raw_output = response.text

        elif llm_config.provider == "openai":
            response = llm_config.client.chat.completions.create(
                model=llm_config.model,
                temperature=0.1,
                messages=[
                    {"role": "system", "content": "Sei un assistente che produce frontmatter YAML valido."},
                    {"role": "user", "content": final_prompt},
                ],
            )
            raw_output = response.choices[0].message.content

        elif llm_config.provider == "claude":
            response = llm_config.client.messages.create(
                model=llm_config.model,
                max_tokens=1024,
                temperature=0,
                messages=[{"role": "user", "content": final_prompt}],
            )
            raw_output = "".join(block.text for block in response.content if getattr(block, "type", "text") == "text")

        else:
            raise ValueError(f"Provider LLM non gestito: {llm_config.provider}")

        if not raw_output:
            return None

        cleaned_response = raw_output.strip().removeprefix("```yaml").removeprefix("```").removesuffix("```").strip()
        return cleaned_response
    except Exception as e:
        print(f"  -> Errore durante la chiamata all'API AI ({llm_config.provider}): {e}")
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

