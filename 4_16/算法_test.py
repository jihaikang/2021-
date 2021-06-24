
# 删除排序数组中的重复项
# nums = [2,1,2,1]
# nums = nums.sort()
# class Solution:
#     def removeDuplicates(self, nums):
        #  逆序删除
        # for i in range(len(nums)-1,0,-1):
        #     if nums[i] == nums[i-1]: # 不啊你这样知识解决了相邻两元素为重复值,这样删除下标也会随着改变
        #         del nums[i]
        # print(len(nums))  # 对了函数尽量使用return别用print
        # print(nums)
        
        # #  正序删除
        # for i in range(len(nums)):
        #     if nums[i] == nums[i+1]:
        #         del nums[i] # 怪不得要逆序,正序删除:这样的话i取最大值，这就无法取nums[i]
        # print(len(nums),nums)


        # 别人的答案
#         i = 0 #  双指针 慢指针i 快指针j
#         for j in range(1, len(nums)):
#             if nums[j] != nums[i]: #  如果我知道每个数组的索引有哪些是重复值是不是就可以删除它，保留一个，或者重新写入一个列表中
#                 i += 1
#                 nums[i] = nums[j] # 这里并没有删除，只是重新写入覆盖
#         return i + 1
#         return nums
#         print(nums)
# a = Solution().removeDuplicates(nums)
