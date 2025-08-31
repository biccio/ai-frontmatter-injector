# **AI Frontmatter Injector for GitHub**

This project is a Python command-line interface (CLI) application that automates the process of enriching technical documentation in Markdown format with structured metadata (frontmatter). The goal goes beyond traditional SEO: the script implements the principles of **Generative Engine Optimization (GEO)**, using the **Schema.org** standard to annotate content with metadata that makes it fully legible and interpretable by modern Artificial Intelligence systems. This transforms the documentation into a foundational knowledge infrastructure for Large Language Models (LLMs) and new AI-driven search experiences.

The script operates directly on GitHub repositories by analyzing files, generating semantically rich frontmatter via AI, and proposing the changes through either a direct push or a Pull Request.

## **Architecture and How It Works**

The core of the system is based on a **Retrieval-Augmented Generation (RAG)** architecture to ensure that the AI's output is accurate, contextual, and compliant with specific standards.

### **1\. AI Core: Google Gemini**

* **Generative Model**: The application uses the **Gemini 1.5 Pro** model via the Google AI API for text analysis and frontmatter block generation.  
* **Embedding Model**: For semantic search, Google's embedding model is used to transform text into numerical vectors.

### **2\. Retrieval: Supabase Vector DB and Schema.org**

* **Vector Database**: To provide the AI with specific and up-to-date knowledge, the system uses a **Supabase** database with the **PostgreSQL pgvector** extension.  
* **Schema.org Indexing**: The entire **Schema.org** vocabulary is processed, converted into vectors (embeddings), and indexed in the Supabase database.  
* **Semantic Search**: When a Markdown file is analyzed, its content is used to perform a vector similarity search on the database. This process retrieves the most relevant Schema.org types and properties for the file's context, which are then provided to the AI.

### **3\. Augmentation: Building the Context**

Before querying the AI, the script builds a detailed and "augmented" prompt that combines several sources of information:

* A **master prompt** that defines the AI's role, objective, and output rules.  
* A **local knowledge base** (/knowledge\_base) containing specific documentation (e.g., the Diataxis framework manual) to contextualize the documentation being analyzed.  
* The **data retrieved from Supabase** (the relevant Schema.org definitions).  
* The **content of the Markdown file** to be processed.  
* **Product information** (name and version) from a configuration file.

### **4\. Generation & GitHub Integration**

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

### **1\. Local Environment Setup**

\# 1\. Clone this repository  
git clone \<URL\_OF\_YOUR\_SCRIPT\_REPO\>  
cd \<SCRIPT\_FOLDER\_NAME\>

\# 2\. Create a virtual environment  
python3 \-m venv venv

\# 3\. Activate the virtual environment  
source venv/bin/activate

\# 4\. Install dependencies  
pip install \-r requirements.txt

### **2\. Credential Configuration (.env)**

Copy the example file .env.example to a new file named .env and enter all the required credentials.

cp .env.example .env

You will need to fill in the following fields:

* GEMINI\_API\_KEY: Your API key for Google Gemini, obtainable from [Google AI Studio](https://aistudio.google.com/app/apikey).  
* SUPABASE\_URL: The URL of your Supabase project.  
* SUPABASE\_KEY: The anon public key of your Supabase project.  
* GITHUB\_TOKEN: A **Personal Access Token (classic)** from GitHub.  
  * **Required Permissions**: Ensure you enable the entire repo scope to allow the script to clone, create forks, and open Pull Requests.

### **3\. Supabase Database Setup**

1. **Create a Project**: Go to [supabase.com](https://supabase.com) and create a new project.  
2. **Enable pgvector**: In the project dashboard, go to Database \> Extensions and enable the vector extension.  
3. **Create the Table**: Go to SQL Editor, open a "New query", and paste and run the contents of the supabase\_setup.sql file provided in this project.  
4. **Index the Knowledge Base**: Run the indexer.py script to populate the database. This will read the files in the /knowledge\_base folder, generate embeddings, and upload them to Supabase.  
   python indexer.py

### **4\. Product Configuration**

Open the config/product\_info.json file and enter the product name and version that the AI should use in the frontmatter.

## **How to Use the Script**

Once the configuration is complete, you can run the script from the terminal (with the virtual environment activated).

### **Base Command**

python github\_main.py \--repo \<owner/repo-name\> \--branch \<branch-name\> \--folder \<path/to/folder\>

### **Arguments**

* \--repo (required): The GitHub repository to work on (e.g., pagopa/devportal-docs).  
* \--branch (optional): The specific branch to analyze. If omitted, the repository's default branch will be used.  
* \--folder (optional): The specific folder within the branch to analyze. If omitted, the entire repository will be analyzed.  
* \--force (optional): A flag that, if present, forces the script to overwrite frontmatter even in files that already have it.

### **Practical Example**

\# Analyze the 'avvisi/guida-tecnica' folder in the 'docs/from-gitbook' branch of the 'pagopa/devportal-docs' repo  
python github\_main.py \--repo pagopa/devportal-docs \--branch docs/from-gitbook \--folder avvisi/guida-tecnica  