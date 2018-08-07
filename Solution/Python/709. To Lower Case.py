class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        start = ord("A")
        last = ord("Z")
        offset = ord("a") - ord("A")
        newStr = ""
        for i in range(len(str)):
            c = str[i]
            asc2 = ord(c)
            if asc2 >= start and asc2 <= last:
                newChar = chr(asc2 + offset)
                newStr += newChar
            else:
                newStr += c
        return newStr


s = "Hello , world!"
res = Solution().toLowerCase(s)
print(res)
