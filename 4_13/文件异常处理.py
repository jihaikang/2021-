# try 语句是正常执行的代码
try:
    # 打开文件（读取中文数据时需要指定 encoding 参数）
    fd = open("a.txt", "r", encoding="UTF-8")
 
    try:
        # 循环一行一行读取文件
        while True:
            line = fd.readline()
 
            # 如果读取结束，退出循环
            if (len(line) == 0):
                break
 
            # 输出读取的数据
            print(line, end="\n")
 
    # 如果在读取文件过程中发生了异常，就会跳入 except 代码块
    # Exception 是所有异常类的基类，Exception as ret 表示为 Exception 类实例化一个对象 ret，
    # ret 对象中就保存了异常的信息；
    except Exception as ret:
        print("读取文件失败，失败原因：", ret)
 
    # 没有发生异常时执行的代码块；如果发生了异常，则不会执行
    else:
        print("读取文件成功")
 
    finally:
        # 不管有没有异常，都会执行 finally 语句
        fd.close()
        print("关闭文件")
 
# except 语句后面也可以不用加异常类
except:
    print("文件不存在")