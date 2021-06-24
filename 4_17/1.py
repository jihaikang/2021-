# 旋转数组

# 循环移位问题
# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
class Solution():
    def shuzu(self,A):
        n = len(A)
        k %= n #  取余
        def reverse(i, j):
            while i < j:
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1

        reverse(0, n - k - 1) #  三次反转
        reverse(n - k, n - 1) # 看不董
        reverse(0, n - 1)

