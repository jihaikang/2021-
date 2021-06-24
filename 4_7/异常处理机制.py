try:
    n1 = int(input('请输入第一个整数：'))
    n2 = int(input('请输入第二个整数：'))
    result = n1/n2 # 这些except是根据程序这行的运行结果来执行判断的
    print('结果为：',result)
    # 这里要输出匹配可以进去的账号密码，并且保存下来
    #保存为一个文件夹
except ZeroDivisionError:
    print('对不起，除数不允许为0')
except ValueError:
    print('只能输入数字串')
except BaseException as e:		#except从子类到父类，最后可以增加BaseException
    print(e)
except Exception as e:
    # print(zidian(key,value))
    #打印出不匹配的之后还要干满来着，把不匹配的值存在一个文件夹里
    # 对还可以借助continue跳出这个循环如果这个值错误的话
    print('cuole2')
print('程序结束')