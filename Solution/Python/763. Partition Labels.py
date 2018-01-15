class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        rangeDict = {}
        for i, c in enumerate(S):
            if c not in rangeDict:
                rangeDict[c] = [i, i]
            else:
                rangeDict[c][1] = i

        rangeList = sorted(rangeDict.values(), key=lambda x: (x[0]))
        ans = []
        cmin = cmax = 0
        for start, end in rangeList:
            if start > cmax:
                ans.append(cmax - cmin + 1)
                cmin, cmax = start, end
            else:
                cmax = max(cmax, end)
        ans.append(cmax - cmin + 1)
        return ans


s = Solution()
res = s.partitionLabels("ababcbacadefegdehijhklij")
print(res)
