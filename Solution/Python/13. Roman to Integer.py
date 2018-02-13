class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman2Int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        i = len(s) - 1
        res = roman2Int[s[i]]
        i -= 1
        while i >= 0:
            if roman2Int[s[i + 1]] > roman2Int[s[i]]:
                res -= roman2Int[s[i]]
            else:
                res += roman2Int[s[i]]
            i -= 1
        return res


solution = Solution()
s = "DCXXI"
res = solution.romanToInt(s)
print(res)
