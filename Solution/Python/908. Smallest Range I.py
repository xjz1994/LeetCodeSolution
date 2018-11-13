class Solution:
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        if len(A) == 1:
            return 0
        minNum = min(A) + K
        maxNum = max(A) - K
        if maxNum - minNum >= 0:
            return maxNum - minNum
        else:
            return 0
