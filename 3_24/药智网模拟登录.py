#测试网址：https://www.yaozh.com/
#测试账号：qq896944660
#初始密码：123456
#请各位同胞手下留情，玩耍完之后请将密码更改为初始密码，以便以下一位同胞也能地愉快玩耍！！！！
 
import requests,re # 源码成功
 
#抓取formhash值（登录表单需要） # 这个post请求都要学的，重点 2021/3/24
def get_formhash(login_url,headers):
        html = requests.get(login_url,headers=headers).text
        p_formhash = r'id="formhash" value="(.+)">'
        formhash = re.findall(p_formhash,html)[0]
         
        return formhash
 
 
#登录与改密
def change_password(login_url,test_url,change_url,headers,formhash):
        #创建会话以保持登录状态
        session = requests.session()
 
        name = input("请输入登录账号：")
        password_prompt = "请输入登录密码："   #密码提示语
        while True:
                password = input(password_prompt)
                #登录账号所需要传输的数据
                form_data = {}
                form_data["username"] = name
                form_data["pwd"] = password
                form_data["formhash"]= formhash
                form_data["backurl"] = "https%3A%2F%2Fwww.yaozh.com%2F"
 
                login_response = session.post(login_url,headers=headers,data=form_data)
                test_response = session.get(test_url,headers=headers)  #test_response 用于验证是否登录成功。
 
                #验证是否登录成功
                if name in test_response.text:
                        print("登录成功")
                        while True:
                                new_password = input("请输入新的登录密码：")
                                re_password = input("请再次输入新的登录密码：")
                                if new_password != re_password:
                                        print("两次密码输入结果不一致，请重新输入！")
                                        continue
                                else:
                                        break
                        #修改密码所所需要提交的数据。
                        change_password_data = {}
                        change_password_data["nowpassword"] =password
                        change_password_data["password"] = new_password
                        change_password_data["repassword"] = re_password
                        change_password_data["issub"] = 1
                        change_response = session.post(change_url,headers=headers,data=change_password_data)
                        print("改密成功")
                        break
                else:
                        password_prompt = ("登录失败，请重新输入登录密码：")
                        continue
 
 
def main():
        login_url = "https://www.yaozh.com/login"
        test_url  = "https://www.yaozh.com/member/"
        change_url = "https://www.yaozh.com/member/uppwd/"
         
        headers = {}
        headers["User-Agent"] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
         
        formhash = get_formhash(login_url,headers)
        change_password(login_url,test_url,change_url,headers,formhash)
 
 
if __name__ == "__main__":
        main()