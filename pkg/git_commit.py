import git
import json
from pathlib import Path


def git_commit(repo_path):
    repo_path = Path(repo_path)
    repo = git.Repo(repo_path)
    g = repo.git
    g.add('.') # git add .
    g.commit('-m', 'Update from Lc-Helper.') # git commit -m "..."
    
    # 获取远程仓库
    remote = repo.remote()
    # 推送本地修改到远程仓库
    remote.push()




if __name__ == "__main__":
    with open("config.json", "r", encoding="utf-8") as f:
        config = json.loads(f.read())
        EMAIL = config['email']
        PASSWORD = config["password"]
        REFRESH = config['refresh']
        REPO_PATH = config["repo_path"]
        GIT_URL = config["git_url"]
        START_ID = config['download_start_id']
        END_ID = config["download_end_id"]
    
    git_commit(REPO_PATH)