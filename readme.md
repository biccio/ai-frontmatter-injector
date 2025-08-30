# **AI Frontmatter Injector per GitHub**

Questo progetto è un'applicazione a riga di comando (CLI) in Python che automatizza l'arricchimento di documentazione tecnica in formato Markdown con metadati strutturati (frontmatter). L'obiettivo va oltre la SEO tradizionale: lo script implementa i principi della **Generative Engine Optimization (GEO)**, utilizzando lo standard **[Schema.org](https://schema.org)** per annotare i contenuti con metadati che li rendono pienamente leggibili e interpretabili dai moderni sistemi di Intelligenza Artificiale. Questo trasforma la documentazione in un'infrastruttura di conoscenza fondamentale per i Large Language Models (LLM) e le nuove esperienze di ricerca basate sull'IA.

Lo script opera direttamente su repository GitHub, analizzando i file, generando un frontmatter semanticamente ricco tramite AI e proponendo le modifiche tramite push diretto o Pull Request.

## **Architettura e Funzionamento**

Il cuore del sistema si basa su un'architettura di **Retrieval-Augmented Generation (RAG)** per garantire che l'output dell'intelligenza artificiale sia accurato, contestuale e aderente a standard specifici.

### **1\. AI Core: Google Gemini**

* **Modello Generativo**: L'applicazione utilizza il modello **Gemini 1.5 Pro** tramite l'API di Google AI per l'analisi del testo e la generazione del blocco frontmatter.  
* **Modello di Embedding**: Per la ricerca semantica, viene utilizzato il modello di embedding di Google per trasformare il testo in vettori numerici.

### **2\. Retrieval: Supabase Vector DB e Schema.org**

* **Database Vettoriale**: Per fornire all'AI una conoscenza specifica e aggiornata, il sistema utilizza un database **Supabase** con l'estensione **PostgreSQL pgvector**.  
* **Indicizzazione di Schema.org**: L'intero vocabolario di **Schema.org** viene processato, trasformato in vettori (embeddings) e indicizzato nel database Supabase.  
* **Ricerca Semantica**: Quando si analizza un file Markdown, il suo contenuto viene usato per eseguire una ricerca di similarità vettoriale sul database. Questo processo recupera i tipi e le proprietà di Schema.org più pertinenti al contesto del file, che verranno poi forniti all'AI.

### **3\. Augmentation: Costruzione del Contesto**

Prima di interrogare l'AI, lo script costruisce un prompt dettagliato e "aumentato" che combina diverse fonti di informazione:

* Un **prompt master** che definisce il ruolo, l'obiettivo e le regole di output per l'AI.  
* Una **knowledge base locale** (/knowledge\_base) contenente documentazione specifica (es. il manuale del framework Diataxis) per contestualizzare la documentazione da analizzare.  
* I **dati recuperati da Supabase** (le definizioni di Schema.org pertinenti).  
* Il **contenuto del file Markdown** da elaborare.  
* Le **informazioni sul prodotto** (nome e versione) da un file di configurazione.

### **4\. Generation & Integrazione GitHub**

L'AI genera il frontmatter in formato YAML, che include un blocco JSON-LD per i metadati di Schema.org. Lo script si occupa quindi di:

* **Clonare il repository** target in un ambiente temporaneo.  
* **Sincronizzare la cronologia** per garantire che le Pull Request siano "pulite" e contengano un solo commit.  
* **Gestire i permessi**:  
  * Se l'utente ha permessi di scrittura, crea un nuovo branch e fa il **push diretto**.  
  * Se l'utente non ha permessi, crea un **fork** del repository e apre una **Pull Request**.  
* **Iniettare il frontmatter** nei file e committare le modifiche in modo selettivo, includendo solo i file effettivamente modificati.

## **Istruzioni per l'Installazione e la Configurazione**

### **Prerequisiti**

* Python 3.9+  
* Git installato sulla macchina locale.

### **1\. Setup dell'Ambiente Locale**

\# 1\. Clona questo repository  
git clone \<URL\_DEL\_TUO\_REPO\_SCRIPT\>  
cd \<NOME\_CARTELLA\_SCRIPT\>

\# 2\. Crea un ambiente virtuale  
python3 \-m venv venv

\# 3\. Attiva l'ambiente virtuale  
source venv/bin/activate

\# 4\. Installa le dipendenze  
pip install \-r requirements.txt

### **2\. Configurazione delle Credenziali (.env)**

Copia il file di esempio .env.example in un nuovo file chiamato .env e inserisci tutte le credenziali necessarie.

cp .env.example .env

Dovrai compilare i seguenti campi:

* GEMINI\_API\_KEY: La tua chiave API per Google Gemini, ottenibile da [Google AI Studio](https://aistudio.google.com/app/apikey).  
* SUPABASE\_URL: L'URL del tuo progetto Supabase.  
* SUPABASE\_KEY: La anon public key del tuo progetto Supabase.  
* GITHUB\_TOKEN: Un **Personal Access Token (classic)** di GitHub.  
  * **Permessi richiesti**: Assicurati di abilitare l'intero scope repo per consentire allo script di clonare, creare fork e aprire Pull Request.

### **3\. Setup del Database Supabase**

1. **Crea un Progetto**: Vai su [supabase.com](https://supabase.com) e crea un nuovo progetto.  
2. **Abilita pgvector**: Nel pannello del progetto, vai su Database \> Extensions e abilita l'estensione vector.  
3. **Crea la Tabella**: Vai su SQL Editor, apri una "New query" e incolla ed esegui il contenuto del file supabase\_setup.sql fornito in questo progetto.  
4. **Indicizza la Knowledge Base**: Esegui lo script indexer.py per popolare il database. Questo leggerà i file nella cartella /knowledge\_base, genererà gli embeddings e li caricherà su Supabase.  
   python indexer.py

### **4\. Configurazione del Prodotto**

Apri il file config/product\_info.json e inserisci il nome e la versione del prodotto che l'AI dovrà usare nel frontmatter.

## **Come Utilizzare lo Script**

Una volta completata la configurazione, puoi lanciare lo script dal terminale (con l'ambiente virtuale attivo).

### **Comando Base**

python github\_main.py \--repo \<owner/repo-name\> \--branch \<branch-name\> \--folder \<path/to/folder\>

### **Argomenti**

* \--repo (obbligatorio): Il repository GitHub su cui lavorare (es. pagopa/devportal-docs).  
* \--branch (opzionale): Il branch specifico da analizzare. Se omesso, verrà utilizzato il branch di default del repository.  
* \--folder (opzionale): La cartella specifica all'interno del branch da analizzare. Se omesso, verrà analizzato l'intero repository.  
* \--force (opzionale): Un flag che, se presente, forza la sovrascrittura del frontmatter anche nei file che ne hanno già uno.

### **Esempio Pratico**

\# Analizza la cartella 'avvisi/guida-tecnica' nel branch 'docs/from-gitbook' del repo 'pagopa/devportal-docs'  
python github\_main.py \--repo pagopa/devportal-docs \--branch docs/from-gitbook \--folder avvisi/guida-tecnica
