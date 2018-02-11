class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = startIndex = 0
        m = {}
        for i in range(len(s)):
            c = s[i]
            if c in m and startIndex <= m[c]:
                startIndex = m[c] + 1
            else:
                res = max(res, i - startIndex + 1)
            m[c] = i
        return res



#s = ""
#s = "a"
#s = "au"
#s = "aabbb"
s = "abcabcbb"
#s = "bbbb"
#s = "pwwkew"
solution = Solution()
res = solution.lengthOfLongestSubstring(s)
print(res)
