class Solution1:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        for i in range(len(s)):
            j = i + len(res) + 1
            while j <= len(s):
                cur = s[i:j]
                if len(cur) > len(res) and cur == cur[::-1]:
                    res = cur
                j += 1
        return res


class Solution2:
    def longestPalindrome(self, s):
        if len(s) == 0:
            return ""
        maxLen = 1
        start = 0
        for i in range(len(s)):
            cur = s[i - maxLen - 1:i + 1]
            if i - maxLen >= 1 and cur == cur[::-1]:
                start = i - maxLen - 1
                maxLen += 2
                continue

            cur = s[i - maxLen:i + 1]
            if i - maxLen >= 0 and cur == cur[::-1]:
                start = i - maxLen
                maxLen += 1

        return s[start:start + maxLen]


s = "babad"
#s = "cbbd"
solution = Solution2()
res = solution.longestPalindrome(s)
# print(res)
