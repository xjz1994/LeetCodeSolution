class Solution(object):
    def findErrorNums(self, nums):
        length = len(nums)
        count = [0] * (length + 1)
        for x in nums:
            count[x] += 1
        for x in range(1, len(nums) + 1):
            if count[x] == 2:
                twice = x
            if count[x] == 0:
                never = x
        return twice, never
