class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 顺时针旋转90度
        n = len(matrix)
        print('矩阵的线性长度：',n)
        # 对角线翻转
        print('对角线翻转')
        for i in range(n - 1):
            print("行的值是：",i)
            print('列循环开始')
            for j in range(i + 1, n):
                print('列的值是：',j)
                print(matrix[i][j])
                print(matrix[j][i])
                print('-'*10)
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        print('水平翻转')
        # 水平翻转
        for i in range(n):
            print("行的值是：",i)
            print('列循环开始')
            for j in range(n >> 1): # 位运算符
                print('列的值是：',j)
                print(matrix[i][j])
                print(matrix[i][n - j - 1])
                print('-'*10)
                matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]
        return matrix
# 其实还没搞懂这算法的规则
# 顺时针转，是吧一定的有规律的对应的矩阵移动到对应的位置吧
# 那这个如果被程序表示出来就叫算法把
matrix = [[1,2,3],[4,5,6],[7,8,9]]
a = Solution()
print(a.rotate(matrix))