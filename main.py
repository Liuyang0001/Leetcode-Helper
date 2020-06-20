import os, sys
import json
from retry import retry
from pathlib import Path
# -------添加环境变量--------------------------
pkg_path = Path(os.getcwd() + '\\pkg\\')
# print(pkg_path)
sys.path.append(pkg_path)
# --------------------------------------------
from pkg.login import login
from pkg.database_maker import database_maker
from pkg.code_downloader import code_downloader
from pkg.readme_maker import readme_maker
from pkg.git_commit import git_commit



class Lc_Helper:

    # 初始化并读取参数
    def __init__(self):
        with open("config.json", "r", encoding="utf-8") as f:
            config = json.loads(f.read())
            self.EMAIL = config['email']
            self.PASSWORD = config["password"]
            self.REFRESH = config['refresh']
            self.REPO_PATH = config["repo_path"]
            self.GIT_URL = config["git_url"]
            self.START_ID = config['download_start_id']
            self.END_ID = config["download_end_id"]

        # 登陆的会话
        self.SESSION = login(self.EMAIL, self.PASSWORD)
        # 建立个人的数据库，仅第一次创建
        # 后面想刷新数据库，请将config中设置为True或者手动删除database
        self.USER_STATE = database_maker(self.SESSION, self.REFRESH)


    # 下载源码
    def codes_download(self):
        self.SESSION=login(self.EMAIL, self.PASSWORD)
        code_downloader(self.SESSION, self.START_ID, self.END_ID, self.REPO_PATH)


    # 建立readme.md
    def build_readme(self):
        readme_maker(self.USER_STATE, self.GIT_URL, self.REPO_PATH)

    
    # 自动提交到github仓库
    def git_commit(self):
        git_commit(self.REPO_PATH)




if __name__ == "__main__":
    lc = Lc_Helper()
    lc.codes_download()
    lc.build_readme()
    lc.git_commit()