import os
import re
import json
import time
import requests
import pandas as pd
from pathlib import Path
from login import login


# 按行写入csv文件
def write_to_csv(id, slug, status, level, vip_only):
    datafile = "database/data.csv"
    # level_dic = {1: "简单", 2: "中等", 3: "困难"}
    columns_ls = ["id", "slug", "status", "level", "vip_only"]
    cont_ls = [{"id": id, "slug": slug, "status": status,
                "level": level, "vip_only": vip_only}]
    df = pd.DataFrame(cont_ls, columns=columns_ls)
    df.to_csv(datafile, index=False, mode="a+", header=False)
    # time.sleep(0.1)


# 调用api获取题目的状态
def get_problems(session, refresh):
    # 用户数据字典
    user_state = {}
    # 获取账号信息api地址
    api_problems_url = "https://leetcode-cn.com/api/problems/all/"
    rec = session.get(api_problems_url)
    # json解析
    rec_json = json.loads(rec.content.decode('utf-8'))
    # 更新用户当前数据
    user_state["user_name"] = rec_json["user_name"]
    user_state["num_solved"] = rec_json["num_solved"]
    user_state["num_total"] = rec_json["num_total"]
    user_state["ac_easy"] = rec_json["ac_easy"]
    user_state["ac_medium"] = rec_json["ac_medium"]
    user_state["ac_hard"] = rec_json["ac_hard"]
    user_state["recent_time"] = time.strftime("%Y-%m-%d %H:%M:%S")
    # 打印一下当前的做题状态
    print("用户：", user_state["user_name"], "已解决：{}/{}".format(
        user_state["num_solved"], user_state["num_total"]))
    
    # 数据路径创建(使用Path不用区分平台)
    datadir = Path("database/")
    datafile = Path("database/data.csv")

    # 如果未创建过数据文件，则第一次必定创建
    if not os.path.exists(datadir):
        refresh = True
        os.makedirs(datadir)
    # 是否更新题库内容
    if not refresh: return user_state
    # 如果已将存在输出文件，先删除再重建
    if os.path.exists(datafile):
        os.remove(datafile)
    
    # 遍历更新题库
    for question in rec_json['stat_status_pairs']:
        id = question['stat']['question_id']  # 题目编号
        slug = question['stat']['question__title_slug']  # 题目名称
        status = question['status']  # 题目状态
        # 题目难度级别，1 为简单，2 为中等，3 为困难
        level = question['difficulty']['level']
        vip_only = question['paid_only']  # 是否为付费题目
        write_to_csv(id, slug, status, level, vip_only)
        print(id, slug,status)  # 当前写入的数据id和名称
    
    return user_state


# 根据slug来获取题目的详细信息
def get_problem_by_slug(session,slug):
    params = {'operationName': "getQuestionDetail",
              'variables': {'titleSlug': slug},
              'query': '''query getQuestionDetail($titleSlug: String!) {
            question(titleSlug: $titleSlug) {
                questionId
                translatedContent
                translatedTitle
                topicTags {
                        translatedName
                }
            }
        }'''
              }
    json_data = json.dumps(params).encode('utf8')
    # 浏览器标识
    user_agent = r"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)"
    headers = {'User-Agent': user_agent, 'Connection':
               'keep-alive', 'Content-Type': 'application/json',
               'Referer': 'https://leetcode-cn.com/problems/' + slug,
               "accept": "*/*",
               "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
               "content-type": "application/json",
               "content-encoding": "gzip, deflate, br"}
    # graphQL api查询
    lc_graphql_url = "https://leetcode-cn.com/graphql"
    resp = session.post(lc_graphql_url, data=json_data, headers=headers, timeout=10)
    content = resp.json()
    # print(content)
    # 题目详细信息
    rec_json = content['data']['question']
    # 中文标签
    tags_cn = [d['translatedName'] for d in rec_json['topicTags'] if d['translatedName']!=None]
    # id = rec_json['questionId']
    title_cn = rec_json['translatedTitle']
    content_cn = rec_json['translatedContent']

    # print(title_cn, content_cn, tags_cn)
    return (title_cn, content_cn, tags_cn)


# 获取当前题目最新提交的id标识
def get_recent_submissions_id(session, slug: str):
    params = {'operationName': "Submissions",
              'variables': {"offset": 0, "limit": 20, "lastKey": '', "questionSlug": slug},
              'query': '''query Submissions($offset: Int!, $limit: Int!, $lastKey: String, $questionSlug: String!) {
                submissionList(offset: $offset, limit: $limit, lastKey: $lastKey, questionSlug: $questionSlug) {
                lastKey
                hasNext
                submissions {
                    id
                    statusDisplay
                    lang
                    url
                    isPending
                }
            }
        }'''
              }
    # print(params)
    json_data = json.dumps(params).encode('utf8')
    # print(json_data)
    # 浏览器标识
    user_agent = r"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)"
    headers = {'User-Agent': user_agent, 'Connection': 'keep-alive',
               "Content-Type": "application/json"}
    # graphql api查询
    lc_graphql_url = "https://leetcode-cn.com/graphql"
    resp = session.post(lc_graphql_url, data=json_data,
                        headers=headers, timeout=10)
    content_json = resp.json()
    # print(content_json)
    try:
        recent_id = content_json['data']['submissionList']['submissions'][0]['id']
        lang = content_json['data']['submissionList']['submissions'][0]['lang']
    except:
        recent_id = None
        lang = ""
    # print(recent_id)
    return (recent_id, lang)


# 建立数据库
def build_database(session, refresh):
    
    datafile = Path("database/data.csv")
    database = Path("database/database.csv")

    # 如果未创建过数据文件，则第一次必定创建
    if not os.path.exists(database):
        refresh = True
    
    # 是否更新题库内容
    if not refresh: return
    
    # 如果已将存在输出文件，先删除再重建
    if os.path.exists(database):
        os.remove(database)

    with open(datafile, "r", encoding="utf-8") as f:
        data = pd.read_csv(f, header=None)
        # print(data)
        for i in range(1, len(data)):
            id, slug, status, level, vip_only = data.iloc[-i]
            
            # if id>100: break # 小规模测试

            # 获取题目的中文信息
            title_cn, content_cn, tags_cn = get_problem_by_slug(session, slug)

            # 题目的描述，如果需要你可以保存下来(html格式)
            # print(content_cn)

            # 只对ac题获取提交id
            if status == "ac":
                submission_id, lang = get_recent_submissions_id(session, slug)
            else: submission_id, lang = "", ""

            columns_ls = ["id", "slug", "status", "level", "vip_only","title_cn","tags_cn", "submission_id", "lang"]
            cont_ls = [
                {
                    "id": id,
                    "slug": slug,
                    "status": status,
                    "level": level,
                    "vip_only": vip_only,
                    "title_cn": title_cn,
                    "tags_cn": ";".join(tags_cn),
                    "submission_id": submission_id,
                    "lang": lang
                }]
            # print(content_cn) # 中文题目描述
            df = pd.DataFrame(cont_ls, columns=columns_ls)
            print(id, title_cn)
            df.to_csv(database, index=False, mode="a+", header=False)


# 建立csv数据库
def database_maker(session, refresh):
    # 获取最新的用户数据字典
    user_state = get_problems(session, refresh)
    # 建立个人数据库
    build_database(session, refresh)
    return user_state


if __name__ == "__main__":
    with open("config.json", "r", encoding="utf-8") as f:
        config = json.loads(f.read())
        EMAIL = config['email']
        PASSWORD = config["password"]
        REFRESH = config['refresh']
        OUTDIR = config["outdir"]
        GIT_URL = config["git_url"]
        START_ID = config['download_start_id']
        END_ID = config["download_end_id"]

    SESSION = login(EMAIL, PASSWORD)
    # 获取最新的用户数据字典
    user_state = get_problems(SESSION, REFRESH)
    # 建立个人数据库
    build_database(SESSION, REFRESH)
