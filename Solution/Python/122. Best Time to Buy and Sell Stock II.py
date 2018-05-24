class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))


prices = [7, 1, 5, 3, 6, 4]
res = Solution().maxProfit(prices)
print(res)
