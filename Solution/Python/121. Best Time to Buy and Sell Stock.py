class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # maxInt
        minPrice = 2**31 - 1
        maxProfit = 0
        for i in prices:
            minPrice = min(i, minPrice)
            maxProfit = max(i - minPrice, maxProfit)
        return maxProfit


s = Solution()
prices = [7, 1, 5, 3, 6, 4]
res = s.maxProfit(prices)
print(res)
