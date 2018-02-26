class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        res = 0
        for i in range(1, N + 1):
            curNum = str(i)
            if '3' in curNum or '4' in curNum or '7' in curNum:
                continue
            if '2' in curNum or '5' in curNum or '6' in curNum or '9' in curNum:
                res += 1
        return res


s = Solution()
res = s.rotatedDigits(10)
print(res)
