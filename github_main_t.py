import argparse
import os
from dotenv import load_dotenv
import git_handler
import file_handler 
import sys
from pathlib import Path
import datetime

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    load_dotenv()

    parser = argparse.ArgumentParser(description="Aggiunge frontmatter AI a file Markdown in un repository GitHub.")
    parser.add_argument("--repo", type=str, required=True, help="Nome del repository GitHub (es. 'owner/repo').")
    parser.add_argument("--branch", type=str, default=None, help="Il branch specifico su cui lavorare (default: branch principale del repo).")
    parser.add_argument("--folder", type=str, default=".", help="La cartella specifica all'interno del repo su cui lavorare (default: root).")
    args = parser.parse_args()

    github_token = os.getenv("GITHUB_TOKEN")
    if not github_token:
        raise SystemExit("Errore: La variabile d'ambiente GITHUB_TOKEN non è impostata.")

    handler = git_handler.GitHandler(github_token)
    temp_dir = git_handler.setup_temp_dir()
    
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    branch_name = f"test/pr-pulita-{timestamp}"
    commit_message = "test: verifica creazione PR pulita"
    pr_title = "Test Creazione PR Pulita"
    pr_body = "Questa PR è stata generata in modalità test per verificare che la sincronizzazione forzata produca una PR con un solo commit."

    try:
        print(f"--- Avvio processo per il repository: {args.repo} ---")
        upstream_repo = handler.get_repo(args.repo)
        source_branch = args.branch if args.branch else upstream_repo.default_branch
        print(f"[+] Branch target: {source_branch}")

        try:
            upstream_repo.get_branch(source_branch)
            print(f"  -> Branch '{source_branch}' trovato.")
        except Exception:
            raise SystemExit(f"Errore: Il branch '{source_branch}' non è stato trovato nel repository '{args.repo}'.")
        
        is_fork = not handler.has_push_access(upstream_repo)
        fork_url = None
        
        if is_fork:
            print("[!] L'utente non ha permessi di scrittura. Procedura di Fork & PR.")
            forked_repo = handler.fork_repo(upstream_repo)
            fork_url = forked_repo.clone_url
        else:
            print("[+] L'utente ha permessi di scrittura. Procedura diretta.")

        # Flusso di lavoro robusto:
        # 1. Clona sempre l'upstream.
        handler.clone_repo(upstream_repo.clone_url, temp_dir, source_branch)
        # 2. Sincronizza la copia locale.
        handler.setup_and_sync_repo(temp_dir, source_branch, fork_url=fork_url)
        # 3. Crea il branch di lavoro da questa base pulita.
        handler.create_branch(temp_dir, branch_name)

        processing_path = os.path.join(temp_dir, args.folder) if args.folder != "." else temp_dir

        # --- MODALITÀ TEST GIT ---
        print("\n[!] MODALITÀ TEST GIT: La logica AI è disattivata.")
        print("    Verrà eseguita una modifica fittizia per testare il flusso Git.")

        markdown_files = file_handler.scan_markdown_files(Path(processing_path))
        if markdown_files:
            test_file_path = markdown_files[0]
            with open(test_file_path, 'a', encoding='utf-8') as f:
                f.write("\n\n<!-- Test commit -->\n")
            print(f"    -> Modifica fittizia aggiunta a: {os.path.relpath(test_file_path, temp_dir)}")
            
            print("\n[+] Finalizzazione delle modifiche su Git...")
            if handler.commit_and_push(temp_dir, branch_name, commit_message, fork_url=fork_url):
                handler.create_pull_request(
                    upstream_repo=upstream_repo, head_branch=branch_name, 
                    base_branch=source_branch, title=pr_title, body=pr_body, is_fork=is_fork
                )
        else:
            print("    -> ATTENZIONE: Nessun file Markdown trovato per la modifica di test.")

    except SystemExit as e:
        print(f"\nERRORE CRITICO: {e}")
    except Exception as e:
        print(f"\nERRORE IMPREVISTO: {e}")
    finally:
        git_handler.cleanup_temp_dir(temp_dir)
        print("\n--- Processo GitHub completato ---")

if __name__ == "__main__":
    main()

