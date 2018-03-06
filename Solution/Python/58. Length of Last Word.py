class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.rstrip(" ").split(" ")[-1])


s = Solution()
#string = "Hello World"
string = "a "
res = s.lengthOfLastWord(string)
print(res)
