class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                s1, s2 = s[l:r], s[l + 1:r + 1]
                return (s1 == s1[::-1]) or (s2 == s2[::-1])
            l += 1
            r -= 1
        return True
