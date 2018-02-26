class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        ans = ma = 0
        for i, x in enumerate(arr):
            ma = max(ma, x)
            if ma == i:
                ans += 1
        return ans


s = Solution()
arr = [4, 3, 2, 1, 0]
#arr = [1, 0, 2, 3, 4]
#arr = [1, 2, 0, 3, 4]
res = s.maxChunksToSorted(arr)
print(res)
