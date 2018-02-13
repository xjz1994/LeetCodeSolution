class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()

        if not len(str):
            return 0

        sign = -1 if str[0] == '-' else 1
        if str[0] in r"+|-":
            str = str[1:]

        numStr = ''
        for i in str:
            if i in "1234567890":
                numStr += i
            else:
                break

        if not len(numStr):
            return 0

        res = sign * int(numStr)
        return max(-2**31, min(res, 2**31 - 1))


s = Solution()
res = s.myAtoi("-2147483648")
print(res)
