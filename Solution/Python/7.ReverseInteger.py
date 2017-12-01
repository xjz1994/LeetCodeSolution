class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        b = (x>0) - (x<0)
        num = b * int(str(abs(x))[::-1])
        if num.bit_length() < 32:
            return num
        else:
            return 0
        
