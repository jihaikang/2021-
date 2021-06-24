# import random  random 返回的是一个实数
# for i in range(1000):
#     print(str(i).zfill(2)) # 这玩意zfill不足用0补，足的话他却不排除
# str = "this is string example....wow!!!"
# print(str.zfill(4))

# 生成任意字符长度的密码

# str='0123456789abcdef_@#$%^'
# base = 22;
# digits = 4;
# try:
#     f = open("cyphers.txt","w")
# except:
#     exit(0)
 
# for i in range(base**digits):
#     pwd = ""
#     num = i
#     for j in range(digits):
#         idx = int(num%base) # 取余
#         num = int(num/base) # 除法向下取整
#         pwd += str[idx]
#     print(pwd,file=f); # 还可以这样写如文件的太厉害了