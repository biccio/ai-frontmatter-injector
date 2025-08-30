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
    
    def _run_command(self, command, working_dir):
        """Helper per eseguire comandi di sistema e gestire errori."""
        try:
            subprocess.run(command, cwd=working_dir, check=True, capture_output=True, text=True)
        except subprocess.CalledProcessError as e:
            print("\n--- ERRORE DURANTE L'ESECUZIONE DI GIT ---")
            print(f"Comando fallito: {' '.join(e.cmd)}")
            print(f"Errore standard:\n{e.stderr}")
            print("------------------------------------")
            raise SystemExit("Operazione Git fallita.")

    def clone_repo(self, repo_url, path, branch):
        print(f"  -> Clonazione del branch '{branch}' da {repo_url}...")
        self._run_command(["git", "clone", "--branch", branch, repo_url, path], working_dir=".")

    def setup_and_sync_repo(self, path, base_branch, fork_url=None):
        print(f"  -> Sincronizzazione forzata del branch di base '{base_branch}'...")
        if fork_url:
            print(f"  -> Aggiunta del remote 'fork': {fork_url}")
            self._run_command(["git", "remote", "add", "fork", fork_url], working_dir=path)
        
        print("  -> Fetch da 'origin'...")
        self._run_command(["git", "fetch", "origin"], working_dir=path)
        
        print(f"  -> Reset forzato di '{base_branch}' a 'origin/{base_branch}'...")
        self._run_command(["git", "checkout", base_branch], working_dir=path)
        self._run_command(["git", "reset", "--hard", f"origin/{base_branch}"], working_dir=path)
        print("  -> Sincronizzazione completata. La base è ora pulita.")

    def create_branch(self, path, branch_name):
        print(f"  -> Creazione del branch di lavoro: '{branch_name}'")
        self._run_command(["git", "checkout", "-b", branch_name], working_dir=path)

    def commit_and_push(self, path, branch_name, message, fork_url=None):
        print("  -> Aggiunta e commit delle modifiche...")
        self._run_command(["git", "add", "."], working_dir=path)
        self._run_command(["git", "commit", "-m", message], working_dir=path)
        
        remote_to_push = 'fork' if fork_url else 'origin'
        print(f"  -> Push delle modifiche sul remote '{remote_to_push}'...")
        self._run_command(["git", "push", "-u", remote_to_push, branch_name], working_dir=path)
        return True

    def create_pull_request(self, upstream_repo, head_branch, base_branch, title, body, is_fork):
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

