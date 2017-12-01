class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :rtype: int
        """        
        if not nums:
        res = 1
        incNum = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                incNum += 1
            else:
                res = max(incNum, res)
                incNum = 1
        return max(incNum, res)
