
# 登录失败,请重新尝试.因该传递的参数改变了，所以呢我要自己构建这些参数重新
#3.需要安装的第三方库: requests
import requests,json,string,re
from urllib.parse import quote
 
#获取电影链接id
def get_movie_id(headers):
    print()
    movie_name_prompt = "请输入电影名称:" #输入提示语
    while True:
        movie_name = input(movie_name_prompt)
        temp_url = "https://movie.douban.com/j/subject_suggest?q={}".format(movie_name) # 看来这个Js已经挂了
        data_url = quote(temp_url, safe=string.printable)  # 网址转码(Python无法识别带中文符号的链接)
        html = requests.get(data_url, headers=headers).text
        data = json.loads(html)
        try: #检测电影名称的有效性
            movie_id = data[0]["id"]
            return movie_id
        except IndexError:
            movie_name_prompt = "检索失败,请重新输入电影名称:"
            continue
 
         
#获取ck值（发表评论表格需要）
def get_ck(session,movie_url):
    html = session.get(movie_url).text
    p_check_id = r'<input type="hidden" name="ck" value="(.+)"/>'
    check_id = re.findall(p_check_id,html)[0]
 
    return check_id
 
 
#登录帐号
def login(session,home_url,login_post_url,headers):
    douban_nickname = input("请输入您的豆瓣名称：") #用于判断是否登录成功
    passnmae_prompt = "请输入您的登录帐号："
    password_prompt = "请输入您的登录密码："
    while True:
        passname = input(passnmae_prompt)
        password = input(password_prompt)
        login_form_data = {}
        login_form_data["ck"] = " "
        login_form_data["name"] = passname
        login_form_data["password"] = password # 以字典形式输入用户名密码等
        login_form_data["remember"] = "false"
        login_form_data["ticket"] = " "
 
        session.post(login_post_url, data=login_form_data, headers=headers)
        check_response_text = session.get(home_url, headers=headers).text
 
        if douban_nickname in check_response_text:
            print()
            print("登录成功")
            return session
        else:
            print()
            print("登录失败,请重新尝试.")
            passnmae_prompt = "请重新输入登录帐号："
            password_prompt = "请重新输入登录密码："
            continue
 
#评论发表
def make_comment(session,movie_comment_post_url,check_id,headers):
    print()
    comment = input("请输入评论内容:")
    #interest = input("请输入您的评论状态(想看/看过)：")
    comment_form_data = {}
    comment_form_data["ck"] = check_id
    comment_form_data["interest"] = "wish"
    #comment_form_data["rating"] = " "  #此处为平分等级,可以添加,但是考虑到显示出来比较麻烦就让他留空了.下tags同
    comment_form_data["foldcollect"] = "F"
    #comment_form_data["tags"] = " "  #此处为便签,
    comment_form_data["comment"] = comment
 
    session.post(movie_comment_post_url,headers=headers,data=comment_form_data)
    check_comment_response_text = session.get(movie_comment_post_url,headers=headers).text
 
    if comment in check_comment_response_text:
        print()
        print("评论成功")
    else:
        print()
        print("评论失败")
 
 
def main():
    home_url = "https://www.douban.com/"
    login_post_url = "https://accounts.douban.com/j/mobile/login/basic"
 
    headers = {}
    headers["User-Agent"] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
 
    session = requests.Session()  #创建回话,以保持登录状态.
    login(session,home_url,login_post_url,headers) #登录帐号
 
    moive_id = get_movie_id(headers) #获取电影id
    movie_comment_post_url = "https://movie.douban.com/j/subject/{}/interest".format(moive_id)
 
    movie_url = "https://movie.douban.com/subject/{}/".format(moive_id)
    check_id = get_ck(session,movie_url)
     
    make_comment(session,movie_comment_post_url,check_id,headers) #发表评论
 
 
if __name__ == "__main__":
    main()