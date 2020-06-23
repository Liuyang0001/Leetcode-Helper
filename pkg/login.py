import json
import requests


# 登陆函数 返回一个登陆的会话
def login(EMAIL,PASSWORD):
    session = requests.Session()  # 建立会话
    session.encoding = "utf-8"
    login_data = {
        'login': EMAIL,
        'password': PASSWORD
    }

    # 浏览器标识
    user_agent = r"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)"
    # 登陆网址
    sign_in_url = 'https://leetcode-cn.com/accounts/login/'
    # lc网址
    leetcode_url = 'https://leetcode-cn.com/'
    headers = {'User-Agent': user_agent, 'Connection': 'keep-alive',
               'Referer': sign_in_url, "origin": leetcode_url}
    
    # 发送登录请求
    session.post(sign_in_url, headers=headers, data=login_data,
                 timeout=10, allow_redirects=False)
    # print(session.cookies)
    is_login = session.cookies.get('LEETCODE_SESSION') != None
    if is_login:
        print("Login successfully!")
        return session
    else: print("Login failed!")



if __name__ == "__main__":
    pass