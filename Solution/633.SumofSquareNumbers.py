class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """        
        maxs = 1
        while(maxs * maxs) < c:
            maxs += 1
 
        low = 0
        high = maxs
        while low <= high:
            if ((low * low) + (high * high)) == c:
                return True
            if ((low * low) + (high * high)) < c:
                low += 1
            if ((low * low) + (high * high)) > c:
                high -= 1
        return False
