class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(1, numRows + 1):
            if i == 1:
                line = [1]
            elif i == 2:
                line = [1, 1]
            else:
                line = [1]
                idx = 1
                while idx < i - 1:
                    line.append(res[i - 2][idx - 1] + res[i - 2][idx])
                    idx += 1
                line.append(1)
            res.append(line)
        return res


numRows = 5
res = Solution().generate(numRows)
print(res)
