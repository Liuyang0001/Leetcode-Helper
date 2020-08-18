import os, sys
import json
from pathlib import Path
# -------添加环境变量--------------------------
# 当前运行文件的文件夹
cur_dir =  os.path.dirname(sys.argv[0])
pkg_path = Path(cur_dir + '/pkg/')
print(pkg_path)
sys.path.append(cur_dir)
sys.path.append(pkg_path)
# --------------------------------------------
# -------导入功能组件--------------------------
from pkg.login import login
from pkg.database_maker import database_maker
from pkg.code_downloader import code_downloader
from pkg.readme_maker import readme_maker
from pkg.git_commit import git_commit
from pkg.get_recent_submissions import get_recent_submissions
# --------------------------------------------


class Lc_Helper:

    # 初始化并读取参数
    def __init__(self):
        # 读取配置
        config_file = Path(cur_dir + "/config.json")
        with open(config_file, "r", encoding="utf-8") as f:
            config = json.loads(f.read())
            self.EMAIL = config['email']
            self.PASSWORD = config["password"]
            self.REFRESH = config['refresh']
            self.REPO_PATH = config["repo_path"]
            self.GIT_URL = config["git_url"]
            self.START_ID = config['download_start_id']
            self.END_ID = config["download_end_id"]
            self.RECENT_NUM = config['get_recent_submissions_nums']
            self.DATABASE_DIR = cur_dir + "/database"
        
        # 登陆的会话
        self.SESSION = login(self.EMAIL, self.PASSWORD)
        # 建立个人的数据库，仅第一次创建
        # 后面想刷新数据库，请将config中设置为True或者手动删除database
        self.USER_STATE = database_maker(self.SESSION, self.REFRESH, self.DATABASE_DIR)


    # 下载源码
    def codes_download(self):
        code_downloader(self.SESSION,self.DATABASE_DIR, self.START_ID, self.END_ID, self.REPO_PATH)


    # 获取最近的提交
    # 局部更新数据库，并下载源码
    def get_recent_submissions(self):
        if not self.REFRESH:
            get_recent_submissions(self.SESSION, self.RECENT_NUM, self.REPO_PATH, self.DATABASE_DIR)

    # 建立readme.md
    def build_readme(self):
        readme_maker(self.USER_STATE, self.GIT_URL, self.REPO_PATH)

    
    # 自动提交到github仓库
    def git_commit(self):
        git_commit(self.REPO_PATH)

    
    # 写点结束语啥的
    def close(self):
        print("\nHave a nice time.")
        print("Bye.")



if __name__ == "__main__":
    lc = Lc_Helper()
    lc.codes_download()
    lc.get_recent_submissions()
    lc.build_readme()
    lc.git_commit()
    lc.close()