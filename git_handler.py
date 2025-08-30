import os
import shutil
import tempfile
from github import Github
import subprocess

class GitHandler:
    def __init__(self, token):
        if not token:
            raise ValueError("È richiesto un token GitHub.")
        self.g = Github(token)
        self.user = self.g.get_user()

    def get_repo(self, repo_name):
        try:
            return self.g.get_repo(repo_name)
        except Exception:
            raise SystemExit(f"Repository '{repo_name}' non trovato o accessibile.")

    def has_push_access(self, repo):
        return repo.permissions.push

    def fork_repo(self, upstream_repo):
        print(f"  -> Creazione del fork di '{upstream_repo.full_name}'...")
        try:
            return self.user.create_fork(upstream_repo)
        except Exception as e:
            if "fork exists" in str(e):
                print("  -> Fork già esistente. Utilizzo quello.")
                return self.g.get_repo(f"{self.user.login}/{upstream_repo.name}")
            raise e
    
    def clone_repo(self, repo_url, path, branch):
        print(f"  -> Clonazione del branch '{branch}' da {repo_url}...")
        try:
            subprocess.run(
                ["git", "clone", "--branch", branch, repo_url, path],
                check=True, capture_output=True
            )
        except subprocess.CalledProcessError as e:
            print(f"Errore standard:\n{e.stderr.decode('utf-8', errors='ignore')}")
            raise SystemExit("Impossibile clonare il repository.")

    def setup_and_sync_repo(self, repo_path, base_branch, fork_url=None):
        print(f"  -> Sincronizzazione forzata del branch di base '{base_branch}' con 'origin'...")
        try:
            if fork_url:
                print(f"  -> Configurazione del remote 'fork' per il push: {fork_url}")
                subprocess.run(["git", "remote", "add", "fork", fork_url], cwd=repo_path, check=True, capture_output=True)
            
            print("  -> Fetch da 'origin'...")
            subprocess.run(["git", "fetch", "origin"], cwd=repo_path, check=True, capture_output=True)
            
            print(f"  -> Checkout del branch di base '{base_branch}'...")
            subprocess.run(["git", "checkout", base_branch], cwd=repo_path, check=True, capture_output=True)

            print(f"  -> Reset forzato di '{base_branch}' a 'origin/{base_branch}'...")
            subprocess.run(
                ["git", "reset", "--hard", f"origin/{base_branch}"],
                cwd=repo_path, check=True, capture_output=True
            )
            print("  -> Sincronizzazione completata. La base è ora pulita.")

        except subprocess.CalledProcessError as e:
            print("\n--- ERRORE DURANTE LA SINCRONIZZAZIONE ---")
            print(f"Comando fallito: {' '.join(e.cmd)}")
            print(f"Errore standard:\n{e.stderr.decode('utf-8', errors='ignore')}")
            print("---------------------------------------")
            raise SystemExit("Impossibile sincronizzare il repository locale.")

    def create_branch(self, repo_path, branch_name):
        print(f"  -> Creazione del branch di lavoro: '{branch_name}'")
        try:
            subprocess.run(
                ["git", "checkout", "-b", branch_name],
                cwd=repo_path, check=True, capture_output=True
            )
        except subprocess.CalledProcessError as e:
            print("\n--- ERRORE DURANTE LA CREAZIONE DEL BRANCH ---")
            print(f"Errore standard:\n{e.stderr.decode('utf-8', errors='ignore')}")
            print("-----------------------------------------")
            raise SystemExit("Impossibile creare il branch di lavoro.")

    # --- FUNZIONE AGGIORNATA per un commit selettivo ---
    def commit_and_push(self, repo_path: str, branch_name: str, message: str, updated_files: list, fork_url: str = None) -> bool:
        try:
            if not updated_files:
                print("  -> Nessun file è stato modificato, nessun commit da creare.")
                return False

            print("  -> Aggiunta selettiva dei file modificati...")
            for file_path in updated_files:
                # Usa percorsi relativi per git add
                relative_path = os.path.relpath(file_path, repo_path)
                subprocess.run(["git", "add", relative_path], cwd=repo_path, check=True, capture_output=True)
            
            print("  -> Esecuzione del commit...")
            subprocess.run(["git", "commit", "-m", message], cwd=repo_path, check=True, capture_output=True)
            
            remote_to_push = 'fork' if fork_url else 'origin'
            print(f"  -> Push delle modifiche sul remote '{remote_to_push}' (branch: '{branch_name}')...")
            
            subprocess.run(
                ["git", "push", "-u", remote_to_push, branch_name],
                cwd=repo_path, check=True, capture_output=True
            )
            
            print("  -> Push completato con successo.")
            return True
        except subprocess.CalledProcessError as e:
            print("\n--- ERRORE DURANTE L'ESECUZIONE DI GIT ---")
            print(f"Comando fallito: {' '.join(e.cmd)}")
            print(f"Errore standard:\n{e.stderr.decode('utf-8', errors='ignore')}")
            print("------------------------------------")
            return False
        except Exception as e:
            print(f"  -> Errore imprevisto durante il commit/push: {e}")
            return False

    def create_pull_request(self, upstream_repo, head_branch, base_branch, title, body, is_fork: bool):
        head_ref = f"{self.user.login}:{head_branch}" if is_fork else head_branch
        
        pulls = upstream_repo.get_pulls(state='open', head=head_ref, base=base_branch)
        if pulls.totalCount > 0:
            print(f"\n[!] Una Pull Request da '{head_ref}' a '{base_branch}' esiste già.")
            print(f"  -> URL: {pulls[0].html_url}")
            return

        print(f"\n[+] Creazione della Pull Request da '{head_ref}' a '{base_branch}'...")
        try:
            pr = upstream_repo.create_pull(
                title=title,
                body=body,
                head=head_ref,
                base=base_branch
            )
            print(f"  -> Pull Request creata con successo!")
            print(f"  -> URL: {pr.html_url}")
        except Exception as e:
            print(f"  -> Errore durante la creazione della Pull Request: {e}")

def setup_temp_dir():
    return tempfile.mkdtemp()

def cleanup_temp_dir(path):
    if os.path.isdir(path):
        shutil.rmtree(path)

