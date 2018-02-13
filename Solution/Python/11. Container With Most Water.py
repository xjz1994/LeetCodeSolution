class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        l = 0
        r = len(height) - 1
        while l < r:
            lVal = height[l]
            rVal = height[r]
            res = max(res, (r - l) * min(lVal, rVal))
            if lVal <= rVal:
                l += 1
            else:
                r -= 1
        return res


s = Solution()
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
res = s.maxArea(height)
print(res)
