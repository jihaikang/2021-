# str1 = '''   *********    '''
# list1 = []
# length = len(str1)
# for i in range(length) :
#     if str1[i] == '\n':
#         continue
#     strleft1 = str(str1[i-3:i])
#     strleft2 = str(str1[i-4:i])
#     strright1 = str(str1[i+1:i+4])
#     strright2 = str(str1[i+1:i+5])
#     if strleft1.isupper() and not strleft2.isupper():
#         if str1[i].islower():
#             if strright1.isupper() and not strright2.isupper():
#                 list1.append(str1[i])
# 打印出来是空列表
# print(list1)

# for循环遍历 #感觉有点像双指针问题 一个子字符串在另一个字符串中出现的次数
def findStr(desStr, subStr):
    count = 0
    length = len(desStr)
    lenth1 = len(subStr)
    if subStr not in desStr:
        print('在目标字符串中未找到字符串!')
    else:
        for each1 in range(length-1):
            # for each2 in range(lenth1-1):
                    # 没理解这里的意思
                if desStr[each1] == subStr[0]: 
                    
                      # 还有这里       这个双if判断好无聊，如果改下
                # 判断是否出现过任意字符 
                # 判断总字符的数量 len
                # 目标字符在总字符索引中迭代
                # 直接用一个总字符的for循环就好了 字符索引是分开的，如何串起来呢
                # 可以用2个for 匹配到该字符则记下该字符索引 然后输出
                # 这样不行啊，是分开的，两字符间的索引是分开的 双for是对的，但不能用if索引来判断吧
                # 如何处理字符前后索引不连串的关系
                    if desStr[each1+1] == subStr[1]:
                        if desStr[each1+2] == subStr[2]:
                            count += 1
                    
        print('子字符串在目标字符串中共出现 %d 次' % count)

desStr = input('请输入目标字符串：')
subStr = input('请输入子字符串(两个字符)：')
findStr(desStr, subStr)
