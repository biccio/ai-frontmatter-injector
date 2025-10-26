# AI Frontmatter Injector

The AI Frontmatter Injector is a Python CLI that enriches Markdown documentation with YAML frontmatter and embedded Schema.org JSON-LD. It is designed for knowledge-base independence: every aspect of the metadata blueprint, taxonomy, and schema hints can be swapped by editing the prompt template and the configuration files inside `knowledge_base/`.

## Key capabilities
- **Retrieval-augmented generation (RAG)** that combines Markdown content, Schema.org references, and custom knowledge-base guidance.
- **Flexible master prompt** that adapts to any documentation model or metadata blueprint by reading configuration snippets from the knowledge base.
- **Automated GitHub workflow** that clones repositories, runs frontmatter injection, and optionally opens Pull Requests.

## How it works
1. `indexer.py` ingests Schema.org definitions into a local ChromaDB collection for semantic retrieval.
2. `knowledge_base/` files (Markdown, YAML, JSON) describe domain-specific rules—such as frontmatter blueprints or allowed taxonomies—that are injected into the master prompt through the `{{KNOWLEDGE_BASE_CONTENT}}` placeholder.
3. `config/master_prompt.txt` defines the AI workflow. The provided template expects the placeholders `{{KNOWLEDGE_BASE_CONTENT}}`, `{{SCHEMA_DEFINITIONS}}`, and `{{MARKDOWN_CONTENT}}`. Customize the knowledge base to change field layouts without touching the prompt.
4. During execution the CLI retrieves relevant Schema.org snippets, assembles the prompt, and generates YAML frontmatter containing a `schema` JSON-LD object.
5. The GitHub integration commits modifications on a branch or fork, depending on repository permissions, and can raise a Pull Request.

## Installation
### Prerequisites
- Python 3.9+
- Git

### Setup
```bash
git clone <repository-url>
cd ai-frontmatter-injector
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Configuration
### Environment variables
Copy `.env.example` to `.env` and fill in provider credentials.
- `LLM_PROVIDER`: `gemini`, `openai`, or `claude`.
- `GEMINI_API_KEY`, `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`: required for the respective LLM providers.
- `EMBEDDING_PROVIDER`: optional override (`google`, `openai`, `sentence-transformers`).
- `CHROMA_DB_PATH`: directory for persisted ChromaDB data (default `./chroma_db`).
- `SENTENCE_TRANSFORMER_MODEL`: model name when using `sentence-transformers` (default `all-MiniLM-L6-v2`).
- `GITHUB_TOKEN`: GitHub Personal Access Token with repo scope.

### Knowledge-base customization
- Add or edit files under `knowledge_base/` to describe documentation rules, frontmatter blueprints, taxonomy values, or schema hints. The repository ships with a neutral `metadata_playbook.md` that defines a generic frontmatter structure and schema hints.
- The runtime concatenates every non-RDF file into the prompt, allowing different clients to provide their own configuration bundles.
- To change behaviour for a specific deployment, replace the knowledge-base directory or inject additional files before running the CLI.

### Schema.org index
Populate the ChromaDB collection with Schema.org entries:
```bash
python indexer.py
```
Ensure that the embedding provider credentials are configured beforehand.

## Usage
Run the GitHub automation from the project root:
```bash
python github_main.py --repo <owner/repo> [--branch <branch>] [--folder <path>] [--force]
```
- `--repo`: target repository (required).
- `--branch`: branch to analyze; defaults to the repo default branch.
- `--folder`: limit processing to a subdirectory.
- `--force`: overwrite existing frontmatter.

## Extending the master prompt
The default `config/master_prompt.txt` aligns with the knowledge-base–driven workflow. To adapt the metadata structure:
1. Define a `frontmatter_blueprint` (or other configuration sections) inside `knowledge_base/` files.
2. Adjust allowed values for document types, roles, or statuses in the same files.
3. Keep the existing placeholders so the runtime can substitute Markdown content and Schema.org definitions.

No automated tests are provided. Validate changes by running the CLI against a sample repository and reviewing the generated frontmatter.
