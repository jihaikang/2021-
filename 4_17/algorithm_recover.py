# algorithm算法

# 买卖股票最佳时间问题
prices = [1,2,3,4,5]
class Solution():
    def price(self,prices):
        profit = 0  # 这里很重要 要给p
        for i in range(1, len(prices)):
            tmp = prices[i] - prices[i - 1] # 这是每天买入第二天卖出
            if tmp > 0: profit += tmp # 只要得到的是两天只差为正我就可以输出
        return profit
        
a = Solution().price(prices)
print(a)

