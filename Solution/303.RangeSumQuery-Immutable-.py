

class NumArray(object):

    summations = []

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.summations = []
        curSum = 0
        for i in nums:
            curSum = curSum + i
            self.summations.append(curSum)
        
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i is 0:
            return self.summations[j]
        else:
            return self.summations[j] - self.summations[i-1]
