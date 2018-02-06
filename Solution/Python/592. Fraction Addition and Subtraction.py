class Solution:
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        import re
        import math
        ints = map(int, re.findall('[+-]?\d+', expression))
        A, B = 0, 1
        for a in ints:
            b = next(ints)
            A = A * b + a * B
            B *= b
            g = math.gcd(A, B)
            A //= g
            B //= g
        return '%d/%d' % (A, B)


s = Solution()

#expression = "-1/2+1/2"
expression = "-1/2+1/2+1/3"
# expression = "1/3-1/2"
# expression = "5/3+1/3"

res = s.fractionAddition(expression)
print(res)
