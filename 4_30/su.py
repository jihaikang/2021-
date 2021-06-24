# 1：排序双指针

# nums1 = [1,2,4,5,6,7]
# nums2 = [2,4,3,7,8,9]
# class Solution():
#     def intersect(nums1,nums2):
#         nums1.sort()
#         nums2.sort()
#         r = []
#         left, right = 0, 0
#         while left < len(nums1) and right < len(nums2):
#             if nums1[left] < nums2[right]:
#                 left += 1
#             elif nums1[left] == nums2[right]:
#                 r.append(nums1[left])
#                 left += 1
#                 right += 1    
#             else:
#                 right += 1
#         return r


# a = Solution.intersect(nums1,nums2)
# print(a)


# 2：给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一  这是不是可以看成高位向低位进位
# [1,3,9]
# 首先思考如何改变一个数组中索引的值
# 这个我看不懂

#         count = 1
#         for i in range(len(digits) - 1, -1, -1):
#             print('列表的索引:',i)
#             print('列表的值：' ,digits[i])
#             count, digits[i] = divmod(digits[i] + count, 10) # 直接赋值可以改变列表的值，小于十的数取余为他本身
#             print('整除后的count:',count)
#             print('取余的:',digits[i])
#             if count == 0:
#                 break 
#         if count:  # 这因该是一种特殊情况，在索引0处再加个0
#             digits.insert(0,count) # 像列表加入元素看不懂，明明是索引0，他却加到后面
            
#         return digits
# # digits = [2,3,7,8,9]
# # for i in range(len(digits) - 1,0, -1):  # 对哦，列表中的range函数下最后一项不执行
# #     print(i)

        # newstr = ''
        # # list -> str
        # for i in digits:
        #     newstr += str(i)
        # # str -> int
        # newnum = int(newstr)
        # newnum += 1
        # # int -> str
        # newnewstr = str(newnum)
        # newlst = []
        # # str -> list
        # for i in newnewstr:
        #     newlst.append(int(i))
        # return newlst


# 3：给定一个数组nums，编写一个函数将所有0移动到数组的末尾，同时保持非零元素的相对顺序
nums = [2,0,3,0,7,19]
class Solution():
    def intersect(digits):
        i = -1
        for j in range(len(nums)):
            print('下标索引j:',j)
            if nums[j]!=0: # 由于一个i的索引是落后于一个j的，所以当j不执行if语句，i就不能自增，所以就导致i，j互换
                i+=1
                print('下标索引i是多少：',i)
                print('i:',nums[i],'\t','j:',nums[j]) 
                print('双指针变换前的列表：',nums)
                nums[i],nums[j]= nums[j], nums[i]
                print('双指针变换后的列表:',nums)
                print('------'*10)
        return nums
a = Solution.intersect(nums)
print(a)
