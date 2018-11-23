class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        i, j = 0, 0
        while i < len(name) and j < len(typed):
            if name[i] == typed[j]:
                i += 1
            elif j == 0 or typed[j] != typed[j-1]:
                return False
            j += 1
        return i == len(name)

# name = "alex"
# typed = "aaleex"

# name = "saeed"
# typed = "ssaaedd"

# name = "leelee"
# typed = "lleeelee"

# name = "laiden"
# typed = "laiden"


name = ""
typed = ""

res = Solution().isLongPressedName(name, typed)
print(res)
