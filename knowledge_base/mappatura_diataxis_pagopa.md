# Mappatura Diataxis PagoPA (v2.4)

Questo documento definisce i principi e la mappatura tassativa del framework Diataxis applicata al sistema documentale di PagoPA. Serve come guida di riferimento per la generazione e la strutturazione di tutti i contenuti tecnici.

## Principi Guida

1.  **Framework Diataxis (v2.4)**: È il fondamento per organizzare i contenuti. La mappatura definita di seguito è rigorosa e specifica per PagoPA.
2.  **Pubblico (User-Centric)**: Il pubblico è composto da **sviluppatori, architetti software e analisti tecnici** dei partner tecnologici. Sono tecnicamente competenti e orientati al risultato (*outcome-driven*).
3.  **Mentalità dell'Utente**: Gli utenti "scansionano" la documentazione per trovare soluzioni rapide a problemi specifici. Non leggono la documentazione per intero.
4.  **Stile (Action-Oriented)**: Il tono è formale ma accessibile.
    * **Voce**: Usa la seconda persona ("tu"). Esempio: "Per ottenere il token, devi inviare una richiesta..."
    * **Titoli**: I titoli dei `Tutorial` e dei `Casi d'uso` iniziano sempre con un verbo all'infinito (es. "Inviare una notifica").
    * **Forma**: Usa la forma attiva.
5.  **Progressive Disclosure**: L'utente riceve solo le informazioni di cui ha bisogno in quel momento. I dettagli tecnici (parametri, errori) non sono duplicati, ma **linkati** dai `Tutorial` e `Casi d'uso` ai `Riferimenti Tecnici`.

## Struttura dei Contenuti (Mapping Diataxis v2.4)

Mapping tassativo tra le sezioni del sistema documentale PagoPA e il framework Diataxis.

---

### Per iniziare

* **Mappatura Diataxis**: `Explanation` + `How-To` (essenziali)
* **Scopo**: Funge da **onboarding obbligatorio** per i nuovi utenti. Non è un sommario, ma un percorso guidato per diventare operativi.
* **Contenuto**:
    1.  **Panoramica (Explanation)**: Spiega cos'è il prodotto e a cosa serve.
    2.  **Tutorial di base (How-To)**: Una sequenza dei primissimi passi indispensabili (es. ottenere credenziali, configurare l'ambiente, effettuare la prima chiamata API).
* **Domanda Utente**: "Sono nuovo, da dove comincio per essere operativo il prima possibile?"

---

### Tutorial

* **Mappatura Diataxis**: `How-To Guide`
* **Scopo**: È il **catalogo delle azioni**. Fornisce una raccolta di guide procedurali, atomiche e focalizzate su un **singolo task**.
* **Contenuto**: Guide step-by-step per risolvere un problema specifico (es. "Creare un avviso", "Verificare uno stato").
* **Struttura**: Obiettivo chiaro, Prerequisiti, Passaggi numerati.
* **Domanda Utente**: "Come faccio a eseguire un task specifico?"

---

### Riferimenti Tecnici

* **Mappatura Diataxis**: `Reference`
* **Scopo**: È l'**enciclopedia dei dettagli** tecnici. Contiene le specifiche precise e funge da unica fonte di verità.
* **Contenuto**: Documentazione delle API (endpoint, parametri, body), modelli di dati, schemi, codici di errore, enumerazioni.
* **Utilizzo**: Non è pensata per essere letta sequenzialmente, ma per essere **consultata tramite link** diretti presenti nei `Tutorial` e nei `Casi d'uso`.
* **Domanda Utente**: "Quali sono le specifiche esatte del parametro X o dell'errore Y?"

---

### Casi d'uso

* **Mappatura Diataxis**: `Tutorial` (nel senso originale di Diataxis: un percorso di apprendimento end-to-end)
* **Scopo**: Mostra come il prodotto risolve **scenari di business reali e complessi**, dall'inizio alla fine.
* **Contenuto**: Percorsi narrativi che spiegano le logiche di un intero processo. **Orchestrano e combinano più `Tutorial` (How-To)** per raggiungere un obiettivo di business completo (es. "Gestire l'intero processo di pagamento di un avviso").
* **Domanda Utente**: "Mostrami un esempio completo di come usare il prodotto per gestire l'intero processo X."