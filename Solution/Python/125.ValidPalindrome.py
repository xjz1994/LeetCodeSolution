class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re
        s = re.sub(r"\W", r"", s.lower())
        return s == s[::-1]
        
