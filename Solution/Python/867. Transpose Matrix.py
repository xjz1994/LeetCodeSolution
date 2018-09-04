class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        rowNum = len(A)
        colNum = len(A[0])
        B = []
        for i in range(colNum):
            newRow = []
            for j in range(rowNum):
                newRow.append(A[j][i])
            B.append(newRow)
        return B


matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
res = Solution().transpose(matrix)
print(res)

# output
# [
#     [1, 4, 7],
#     [2, 5, 8],
#     [3, 6, 9]
# ]
