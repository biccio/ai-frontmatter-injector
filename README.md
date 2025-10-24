# **AI Frontmatter Injector for GitHub**

This project is a Python command-line interface (CLI) application that automates the process of enriching technical documentation in Markdown format with structured metadata (frontmatter). The goal goes beyond traditional SEO: the script implements the principles of **Generative Engine Optimization (GEO)**, using the **Schema.org** standard to annotate content with metadata that makes it fully legible and interpretable by modern Artificial Intelligence systems. This transforms the documentation into a foundational knowledge infrastructure for Large Language Models (LLMs) and new AI-driven search experiences.

The script operates directly on GitHub repositories by analyzing files, generating semantically rich frontmatter via AI, and proposing the changes through either a direct push or a Pull Request.

## **Architecture and How It Works**

The core of the system is based on a **Retrieval-Augmented Generation (RAG)** architecture to ensure that the AI's output is accurate, contextual, and compliant with specific standards.

### **1. AI Core: Multi-provider LLMs**

* **Generative Models**: The application can run on **OpenAI (GPT-4o family)**, **Google Gemini (Gemini 2.5 Pro by default)**, or **Anthropic Claude (Claude 3.5 Sonnet by default)**. Select the provider via the `LLM_PROVIDER` environment variable.
* **Embedding Models**: Vector embeddings are produced through ChromaDB's pluggable embedding functions. You can reuse the same provider selected for generation or choose another one through the `EMBEDDING_PROVIDER` variable (`google`, `openai`, or `sentence-transformers`).

### **2. Retrieval: ChromaDB Vector Store and Schema.org**

* **Vector Database**: All embeddings are stored in a local (or configurable) **ChromaDB** collection, which keeps the knowledge base close to the CLI without external dependencies.
* **Schema.org Indexing**: The `indexer.py` script processes the Schema.org vocabulary, converts each class/property into embeddings, and upserts them into ChromaDB.
* **Semantic Search**: When a Markdown file is analyzed, its content is embedded and matched against ChromaDB to retrieve the most relevant Schema.org types and properties. These snippets are then provided to the LLM as additional context.

### **3. Augmentation: Building the Context**

Before querying the AI, the script builds a detailed and "augmented" prompt that combines several sources of information:

* A **master prompt** that defines the AI's role, objective, and output rules.  
* A **local knowledge base** (`/knowledge_base`) containing specific documentation to contextualize the documentation being analyzed.  
* The **data retrieved from ChromaDB** (the relevant Schema.org definitions).
* The **content of the Markdown file** to be processed.  
* **Product information** (name and version) from a configuration file.

### **4. Generation & GitHub Integration**

The AI generates the frontmatter in YAML format, which includes a JSON-LD block for Schema.org metadata. The script then handles the following:

* **Cloning the repository** into a temporary environment.  
* **Synchronizing the history** to ensure Pull Requests are "clean" and contain only a single commit.  
* **Handling permissions**:  
  * If the user has write permissions, it creates a new branch and performs a **direct push**.  
  * If the user does not have permissions, it creates a **fork** of the repository and opens a **Pull Request**.  
* **Injecting the frontmatter** into the files and selectively committing the changes, including only the files that were actually modified.

## **Installation and Configuration Instructions**

### **Prerequisites**

* Python 3.9+  
* Git installed on the local machine.

### **1. Local Environment Setup**

#### 1. Clone this repository  
```
git clone <URL_OF_YOUR_SCRIPT_REPO>  
cd <SCRIPT_FOLDER_NAME>
```
#### 2. Create a virtual environment  
`python3 -m venv venv`

#### 3. Activate the virtual environment  
`source venv/bin/activate`

#### 4. Install dependencies  
`pip install -r requirements.txt`

### **2. Credential Configuration (.env)**

Copy the example file .env.example to a new file named .env and enter all the required credentials.

`cp .env.example .env`

You will need to fill in the following fields:

* `LLM_PROVIDER`: Choose which provider to use (`gemini`, `openai`, or `claude`).
* `GEMINI_API_KEY`: Required when using Gemini as LLM or when `EMBEDDING_PROVIDER=google`.
* `OPENAI_API_KEY`: Required when using OpenAI as LLM or when `EMBEDDING_PROVIDER=openai`.
* `ANTHROPIC_API_KEY`: Required when using Claude as LLM.
* `EMBEDDING_PROVIDER` *(optional)*: Override the embedding backend. Supported values are `google`, `openai`, and `sentence-transformers`. Defaults to a sensible value based on the chosen LLM.
* `CHROMA_DB_PATH` *(optional)*: Filesystem path where ChromaDB should persist data. Defaults to `./chroma_db` inside the project.
* `SENTENCE_TRANSFORMER_MODEL` *(optional)*: Model name to use when `EMBEDDING_PROVIDER=sentence-transformers` (default: `all-MiniLM-L6-v2`).
* `GITHUB_TOKEN`: A **Personal Access Token (classic)** from GitHub.
  * **Required Permissions**: Ensure you enable the entire repo scope to allow the script to clone, create forks, and open Pull Requests.

### **3. ChromaDB Index Setup**

ChromaDB runs locally, so no external database configuration is required. To populate the vector store:

1. Ensure the environment variables for your chosen embedding provider are set (for example `EMBEDDING_PROVIDER` and the corresponding API keys).
2. Run `python indexer.py` to parse the Schema.org knowledge base and upsert embeddings into ChromaDB. The persistent files are stored in the directory specified by `CHROMA_DB_PATH`.

### **4. Product Configuration**

Open the `config/product_info.json` file and enter the product name and version that the AI should use in the frontmatter.

## **How to Use the Script**

Once the configuration is complete, you can run the script from the terminal (with the virtual environment activated).

### **Base Command**

`python github_main.py --repo <owner/repo-name> --branch <branch-name> --folder <path/to/folder>`

### **Arguments**

* `--repo` (required): The GitHub repository to work on (e.g., pagopa/devportal-docs).  
* `--branch` (optional): The specific branch to analyze. If omitted, the repository's default branch will be used.  
* `--folder` (optional): The specific folder within the branch to analyze. If omitted, the entire repository will be analyzed.  
* `--force` (optional): A flag that, if present, forces the script to overwrite frontmatter even in files that already have it.

