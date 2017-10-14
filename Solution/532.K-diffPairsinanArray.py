


class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0: return 0
        count = 0
        d = dict()
        for num in nums:
            if(num in d):
                d[num] = d[num] + 1
            else:
                d[num] = 1

        for item in d:
            if k == 0 :
                if d[item] >= 2:
                    count = count + 1
            else: 
                if item+k in d:
                    count = count + 1
        return count
