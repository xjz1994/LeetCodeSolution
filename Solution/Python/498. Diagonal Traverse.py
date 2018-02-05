class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        res = []
        lines = []

        def addLine(row, col):
            res = []
            while row < len(matrix) and col >= 0:
                res.append(matrix[row][col])
                row += 1
                col -= 1
            lines.append(res)

        for i in range(len(matrix[0])):
            addLine(0, i)
        for i in range(1, len(matrix)):
            addLine(i, len(matrix[i]) - 1)

        isRe = 1
        for i in lines:
            l = len(res)
            if isRe:
                res[l:l] = i[::-1]
            else:
                res[l:l] = i
            isRe ^= 1
        return res


matrix = [
    [3],
    [2]
]
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

s = Solution()
res = s.findDiagonalOrder(matrix)
print(res)
