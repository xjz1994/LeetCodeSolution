class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        res, curSum = nums[0], 0
        for i in nums:
            if curSum < 0:
                curSum = i
            else:
                curSum += i
            res = max(res, curSum)
        return res


s = Solution()
# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# expected = 6

nums = [-1]
expected = -1
res = s.maxSubArray(nums)
print(res == expected)
