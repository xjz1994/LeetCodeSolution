class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        I = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        X = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        C = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        M = ['', 'M', 'MM', 'MMM']
        thousand = num // 1000
        houndred = (num % 1000) // 100
        ten = (num % 100) // 10
        digit = num % 10
        return M[thousand] + C[houndred] + X[ten] + I[digit]


s = Solution()
# num = 1
# num = 19
# num = 99
# num = 100
num = 409
#num = 1999
res = s.intToRoman(num)
print(res)
