class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1 / x
            n = -n

        res = 1
        while n:
            if n & 1 == True:
                res *= x
            x *= x
            n //= 2
        return res


s = Solution()
res = s.myPow(2, 10)
print(res)
