# Leetcode-Helper 

<p> 
<img src="https://badgen.net/badge/Coder/Mr.Liu/red?icon=github" alt="">
<img src="https://badgen.net/badge/Python/3.7.6/yellow?" alt="">
<img src="https://badgen.net/badge/pandas/1.0.1/green?" alt="">
<img src="https://badgen.net/badge/requests/2.22.0/blue?" alt="">
</p>



哪个程序员😁不想一键下载写过的代码，自动上传Github，并且还能生成一份好看的README呢？

真的有人会不点⭐吗?  不会吧，不会吧，不会吧。


<hr>


**💕主要功能💕**

🍉 模拟登陆力扣中国站(leetcode-cn)

🍉 爬取每题提交的ac代码，保存至本地。

🍉 自动生成优美的README文件至本地。

🍉 支持自动更新至Github仓库。 🆕

🍉 加入失败重试机制，减少延时，加快下载速度。🆕




<hr>


**少啰嗦，先看东西 :   [具体效果,点击这里 ](https://github.com/Liuyang0001/LeetCode_By_Python)** 😃 


生成的README效果图：

![](https://gitee.com/liuyang0001/blogimage/raw/master/img/20200613133201.png)



生成的源码效果图：

![](https://gitee.com/liuyang0001/blogimage/raw/master/img/20200619174224.png)



<hr>

## 使用说明

1. **clone 该项目到你的本地。**

```python
git clone https://github.com/Liuyang0001/Leetcode-Helper.git
```

2. **配置你的cofig.json文件。**

```json
{
    "email": "xx账号xxxx",
    "password": "xxx密码xxx",
    "repo_path": "x:/xxxxxx/",
    "git_url": "https://github.com/xxxxx/xxx仓库名xx/tree/master/codes_auto/",
    "download_start_id": 1, 
    "download_end_id": 10000,
    "refresh": false
}
```

3. **安装依赖库**

依赖库为`retry` ，`pandas` ，`requests`，`gitpython`可自行安装，或者使用：

```
pip install -r requirement.txt
```

4. **运行`main.py`文件**

```
python main.py
```



<hr>

> 其他说明：
>
> 1. 第一次运行比较慢，主要是需要建立本地数据库，请耐心等待。
> 2. 题库后续会增加局部更新，就不用每次都全局更新，请持续关注。
> 3. ~~如果发生异常，请尝试重新运行 。~~   已加入失败重试机制。
> 4. 为了运行速度，已生成代码不会覆盖，相同题的代码仅保留一份ac的。
> 5. 如果大家有需求的话，可能还会写个GUI界面，会更直观一点，没人的话就算了。




本人是一个准研一的小菜🐔，在家无事的练手项目，求轻喷。

万水千山总是情，给个⭐行不行，感谢大家。

Enjoy coding！
