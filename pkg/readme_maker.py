import os
import json
import pandas as pd
from pathlib import Path
from pkg.login import login
from pkg.database_maker import get_problems


# 生成表格上方的内容
def head_maker(user_state, outdir):
    # print(user_state)
    ls = [
        '# Stay hangury ，Stay foolish \n\n',
        '<p> \n',
        '<img src=\"https://img.shields.io/badge/User-{}-purple.svg?\" alt=\"\">\n'.format(
            user_state['user_name']),
        '<img src=\"https://img.shields.io/badge/Solved-{}/{}-blue.svg?\" alt=\"\">\n'.format(
            user_state["num_solved"], user_state["num_total"]),
        '<img src=\"https://img.shields.io/badge/Easy-{}-yellow.svg?\" alt=\"\">\n'.format(
            user_state["ac_easy"]),
        '<img src=\"https://img.shields.io/badge/Medium-{}-green.svg?\" alt=\"\">\n'.format(
            user_state["ac_medium"]),
        '<img src=\"https://img.shields.io/badge/Hard-{}-red.svg?\" alt=\"\">\n'.format(
            user_state["ac_hard"]),
        '</p> \n\n',
        ':heart: 最近一次更新:  {}  \n\n'.format(user_state["recent_time"]),
        ':heart: 题目后带有 :lock: 表示该题尚未解锁，需要购买力扣经典会员。\n\n',
        ':heart: 本README文件与源码文件均为自动生成，详情见爬虫项目[Leetcode-Helper](https://github.com/Liuyang0001/Leetcode-Helper)。\n\n',
        '\n\n<hr>\n\n'
    ]
    text = "".join(ls)
    # print(text)
    # return text

    # 把text写进readme
    md_path = Path(outdir+"/README.md")
    with open(md_path, "w+", encoding="utf-8") as md:
        md.writelines(text)


# 生成表格内容
def grids_maker(git_url, outdir):
    grids_head = [
        "|  题号  |     题目     |   难度  |   标签   |   源码   | \n",
        "| :----: | :--------: | :----: | :------: | :------: | \n",
    ]
    datafile = Path("database/database.csv")
    md_path = Path(outdir+"/README.md")
    with open(datafile, "r", encoding="utf-8") as f:
        data = pd.read_csv(f)
        with open(md_path, "a+", encoding="utf-8") as md:
            md.writelines(grids_head)
            for i in range(len(data)):
                id, slug, status, level, vip_only, title_cn, tags_cn, \
                        submission_id, lang = data.iloc[i]
                # 后面在数据库加上最新提交的语言和提交id
                if id > 2000: break # 暂时先不要后面的题目,想要生成de屏蔽此条
                # print(id, slug, status, level, vip_only, title_cn, tags_cn)
                # print(type(tags_cn)==float)
                level = ["", "简单", "中等", "困难"][level]
                if type(tags_cn) == float:
                    tags_cn = "暂无标签"
                if type(title_cn) == float:
                    title_cn = "害-未爬到中文名"
                if vip_only:
                    title_cn += " :lock:"
                else:
                    title_cn = f"[{title_cn}](https://leetcode-cn.com/problems/{slug})"
                lang_dic = {
                    "python3": ".py",
                    "python": ".py",
                    "java": ".java",
                    "cpp": ".cpp",
                    "c": ".c"}
                lang_post = lang_dic.get(lang, "")
                if lang=="python3": lang="python"
                if status == "ac":
                    source = f"[{lang.title()}]({git_url}{id}.{slug}{lang_post})"
                else:
                    source = "To Do"
                line = f"|{id}|{title_cn}|{level}|{tags_cn}|{source}|\n"
                # print(line)
                md.write(line)


# 生成md文件
def readme_maker(user_state, git_url, outdir):
    print("# Start building README.md...")
    head_maker(user_state, outdir)
    grids_maker(git_url, outdir)
    print("  Done.")
    print("--------------------------------------------")



if __name__ == "__main__":
    pass
