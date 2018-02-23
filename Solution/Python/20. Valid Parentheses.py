class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pair = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        stack = []
        for i in s:
            if i in pair.values():
                stack.append(i)
            elif i in pair.keys():
                if len(stack) == 0 or pair[i] != stack.pop():
                    return False
            else:
                return False

        return len(stack) == 0


solution = Solution()
s = "()[]{}"
res = solution.isValid(s)
print(res)
