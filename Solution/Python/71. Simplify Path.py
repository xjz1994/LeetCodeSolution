class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        pathArr = path.split("/")
        for i in pathArr:
            if i == "." or i == "":
                continue
            if i == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(i)

        return "/" + "/".join(stack)


s = Solution()
#path = "/home/"
#path = "/a/./b/../../c/"
path = "/.."
res = s.simplifyPath(path)
print(res)
