import json
import os
import sys
import time
import pandas as pd
from pathlib import Path
from pkg.login import login
from pkg.code_downloader import write_code_to_file


# 从最近提交的内容提取有效的部分
def get_useful_information(session, num:int)->dict:
    submissions_dic = {}
    n = num//20 if not num%20 else num//20+1
    last_key = ""
    for _ in range(n):
        url = f"https://leetcode-cn.com/api/submissions/?lastkey={last_key}"
        # print(url)
        rec = session.get(url)
        # json解析
        rec_json = json.loads(rec.content.decode('utf-8'))
        # print(rec_json)
        submissions = rec_json["submissions_dump"]
        # "has_next":true,"last_key":"xrjjr4l1m"
        has_next = rec_json["has_next"]
        last_key = rec_json["last_key"] if has_next else ""
        # print(len(submissions))
        for submission in submissions:
            # "id":80752913,
            # "lang":"python3",
            # "time":"7 小时，20 分钟",
            # "status_display":"Accepted",
            # "runtime":"156 ms",
            # "url":"/submissions/detail/80752913/",
            # "is_pending":"Not Pending",
            # "title":"保证文件名唯一",
            # "timestamp":1592712662,
            # "memory":"26.8 MB",
            # "code":"class..

            title_cn = submission["title"]
            # 只保留最新的一份ac
            if title_cn in submissions_dic: continue
            # 除去非ac的部分提交
            if submission["status_display"]=="Accepted":
                submissions_dic[title_cn] = submission
            else: continue
        if not has_next: break
        time.sleep(1) # 必须加延时，不然会报错“没有权限”
    # print(submissions_dic)
    return submissions_dic



def save_from_dic(submissions_dic, repo_path):
    database = Path("database/database.csv")
    df = pd.read_csv(database, encoding="utf-8")
    df = df.astype(str)
    for title in submissions_dic.keys():
        # print(title)
        # ————————————查询数据库—————————————————————
        cur = df[df.title_cn == title]
        if len(cur) == 0: continue  # 未查询到该项
        # 查询当前值对应的id和英文名
        id = cur.id.values[0]
        slug = cur.slug.values[0]
        # ——————————————————————————————————————————


        # ————————————修改数据库————————————————————
        df.loc[cur.index, 'status'] = 'ac'
        df.loc[cur.index, 'submission_id'] = submissions_dic[title]['id']
        df.loc[cur.index, 'lang'] = submissions_dic[title]['lang']
        df.to_csv(database,index=None) # 更新修改至csv
        # ——————————————————————————————————————————
        # 获取提交的语言
        lang = submissions_dic[title]['lang']
        lang_dic = {
            "python3": ".py",
            "python": ".py",
            "java": ".java",
            "cpp": ".cpp",
            "c": ".c",
            "bash": ".sh"
        }
        code_file = repo_path + "/codes_auto/" + str(int(id)) + "." + slug + lang_dic.get(lang,"")
        code_file = Path(code_file) # 格式化path
        if os.path.exists(code_file): continue
        code = submissions_dic[title]["code"]
        # 已经存在一份ac解，则跳过
        print(f"[{id}.{slug}.{lang}]")
        write_code_to_file(code, code_file, str(int(id)), slug, lang)
        time.sleep(0.1)  


def get_recent_submissions(session, recent_num, repo_path):
    print("# Start geting recent submissions...")
    submissions_dic = get_useful_information(session, recent_num)
    save_from_dic(submissions_dic, repo_path)
    print("  Done.")
    print("--------------------------------------------")





if __name__ == "__main__":
    pass
    
