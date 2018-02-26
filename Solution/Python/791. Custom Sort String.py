class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        res = ""
        sDict = {}
        for i in S:
            sDict[i] = sDict[i] + 1 if sDict.get(i) else 1

        tDict = {}
        for i in T:
            tDict[i] = tDict[i] + 1 if tDict.get(i) else 1

        for i in S:
            if i in tDict:
                res += i * tDict[i]
        for i in T:
            if not i in sDict:
                res += i
        return res


s = Solution()
# S = "cba"
# T = "abcd"
S = "kqep"
T = "pekeq"
res = s.customSortString(S, T)
print(res)
