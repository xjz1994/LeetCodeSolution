class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set(nums)
        if(len(s) > 2):
            s.remove(max(s))
            s.remove(max(s))
            return max(s)
        else:
            return max(s)
