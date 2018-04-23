class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []

        def gen(curIndex, path):
            if path and len(path) > 4:
                return
            if curIndex == len(s) and len(path) == 4:
                res.append(".".join(path[:]))
            for i in range(curIndex + 1, min(len(s) + 1, curIndex + 4)):
                nextStr = s[curIndex:i]
                nextNum = int(nextStr)
                if str(nextNum) == nextStr and nextNum <= 255:
                    gen(i, path + [nextStr])

        gen(0, [])
        return res


s = "25525511135"
#s = "0000"
#s = "010010"
solution = Solution()
res = solution.restoreIpAddresses(s)
print(res)
