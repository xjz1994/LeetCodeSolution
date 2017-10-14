class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        sum = 0
        curSum = 0
        addNum = 0
        for i in range(0, len(nums)):
            if addNum < k:
                curSum += nums[i]
                sum = curSum
                addNum += 1
            else:
                curSum = curSum - nums[i - k] + nums[i]
                sum = max(sum, curSum)
        return sum * 1.0 / k
