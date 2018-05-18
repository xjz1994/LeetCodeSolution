class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = []
        if rowIndex >= 0:
            res.append(1)
        if rowIndex >= 1:
            res.append(1)
        for idx in range(2, rowIndex + 1):
            res.append(1)
            for i in range(idx - 1, 0, -1):
                res[i] = res[i] + res[i - 1]
        return res


rowIndex = 4
res = Solution().getRow(rowIndex)
print(res)
