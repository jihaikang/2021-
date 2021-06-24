# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，
# 并返回它们的数组下标。
# def TwoSums(board,List):
#    lens = len(nums)
#     j=-1
#     for i in range(lens):
#         if (target - nums[i]) in nums:
#             if (nums.count(target - nums[i]) == 1)&(target - nums[i] == nums[i]):#如果num2=num1,且nums中只出现了一次，说明找到是num1本身。
#                 # count始匹配对应的字符串的索引  # 
#                 continue

#             else:
#                 j = nums.index(target - nums[i],i+1) #index(x,i+1)是从num1后的序列后找num2                
#                 break
#     if j>0:
#         return [i,j]
#     else:
#         return []

#  分割线--------------
#     hashmap={}
#     for ind,num in enumerate(nums)： # enumerate作用是遍历列表，生成对应序列号和值
#         print('ind',ind,'num',num)
#         hashmap[num] = ind
#         print('打印出现在的字典')
#         print(hashmap)
#         print('-'*10)
#     for i,num in enumerate(nums):
#         print('i:',i,'num',num)
#         j = hashmap.get(target - num)  # get是从字典中的键获取值
#         print('j：',j)
#         if j is not None and i!=j:
#             return [i,j]
# nums = [2,7,11,15]
# target = 9
# a = TwoSums(nums,target)
# print(a)
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board):
       # 解法一
        # n = len(board)
        # print('board的长度是多少:',n)
        # m = len(board[0])
        # print('len(board[0]):',m)
        # row = [[] * 9 for _ in range(9)] # 生成简单的列表 
        # print(row)
        # col = [[] * 9 for _ in range(9)]
        # print(col)
        # nine = [[] * 9 for _ in range(9)]
        # print(nine)
        # for i in range(n):
        #     print(i)
        #     for j in range(m):
        #         tmp = board[i][j] #  具体九宫格数据
        #         print('i:',i,'\n','j:',j)
        #         print('tmp:',tmp)
        #         if not tmp.isdigit(): #检验tem是否有数字组成
        #             continue
        #         if tmp in row[i]:
        #             return False
        #         if tmp in col[j]:
        #             return False
        #         if tmp in nine[(j // 3) * 3 + (i // 3)]:
        #             return False
        #         row[i].append(tmp)
        #         print('row:',row)
        #         col[j].append(tmp)
        #         print('col:',col)
        #         print((j // 3) * 3 + (i // 3))
        #         nine[(j // 3) * 3 + (i // 3)].append(tmp)
        #         print('nine:',nine)
        # return True

        # 解法二
        lows, columns, boxes = defaultdict(set), defaultdict(set), defaultdict(set) # 将其转化为集合，集合是不允许
        # 有重复值的
        print(lows)
        print(columns)
        print(boxes)

        for low in range(9):
            for col in range(9): 
                print('九宫格数据是：',board[low][col] )
                print('行的数据是：',lows[low])
                print('列的数据是：',columns[col])
                print('3*3宫格的数据是：',boxes[low // 3, col // 3])
                print('-'*10)
                if board[low][col].isdigit(): # 或者用 board[low][col] != '.'也可以
                    #以下三个if判断是不是在行、列和 3*3宫格内存在有重复数字*
                    if board[low][col] in lows[low]:
                        return False
                    if board[low][col] in columns[col]:
                        return False
                    #这里3*3宫格缩小1/3*
                    if board[low][col] in boxes[low // 3, col // 3]:
                        return False
                    #没存在加入行、列和 3*3宫格*
                    lows[low].add(board[low][col])
                    columns[col].add(board[low][col])
                    boxes[low // 3, col // 3].add(board[low][col])
                    
        return True


board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

a = Solution()
a.isValidSudoku(board)
