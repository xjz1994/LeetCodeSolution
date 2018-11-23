class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def getRes(string):
            res = ""
            idx = len(string) - 1
            backNum = 0
            while idx >= 0:
                cur = string[idx]
                if cur == "#":
                    backNum += 1
                else:
                    if backNum > 0:
                        backNum -= 1
                    else:
                        res = cur + res
                idx -= 1
            return res

        sRes = getRes(S)
        tRes = getRes(T)
        return sRes == tRes


class Solution2(object):
    def backspaceCompare(self, S, T):
                def getRes(string):
            res = []
            for i in range(0, len(string)):
                cur = string[i]
                if cur == "#":
                    if len(res) > 0:
                        res.pop()
                else:
                    res.append(cur)
            return res

        sRes = getRes(S)
        tRes = getRes(T)

        return sRes == tRes

S = "aaab##"
T = "c#d#"

res = Solution().backspaceCompare(S, T)
print(res)
