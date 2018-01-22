class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False

        rowNum = max(0, len(matrix) - 1)
        colNum = max(0, len(matrix[0]) - 1)

        if rowNum is 0 or colNum is 0:
            return True

        for i in range(rowNum):
            for j in range(colNum):
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
        return True
# matrix = [
#     [1, 2, 3, 4],
#     [5, 1, 2, 3],
#     [9, 5, 1, 2]
# ]


# matrix = [
#     [1, 2],
#     [2, 2]
# ]


matrix = [
    [39, 24],
    [24, 39],
    [65, 24]
]

#matrix = [[10], [11], [12]]

s = Solution()
res = s.isToeplitzMatrix(matrix)
print(res)
