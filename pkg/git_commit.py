import git
import json
from pathlib import Path


def git_commit(repo_path):
    print("# Start committing to the remote repository...")
    repo_path = Path(repo_path)
    repo = git.Repo(repo_path)
    g = repo.git
    g.add('.') # git add .
    g.commit('-m', 'Update from Lc-Helper.') # git commit -m "..."
    
    # 获取远程仓库
    remote = repo.remote()
    # 推送本地修改到远程仓库
    remote.push()
    print("  Done.")
    print("--------------------------------------------")



if __name__ == "__main__":
    pass 