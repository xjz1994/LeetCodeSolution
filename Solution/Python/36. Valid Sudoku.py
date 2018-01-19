class Solution:
    def valid3by3(self, board, row, col):
        validPos = [
            [-1, -1], [-1, 0], [-1, 1],
            [0, -1], [0, 0], [0, 1],
            [1, -1], [1, 0], [1, 1]
        ]
        s = set()
        for pos in validPos:
            curVal = board[row + pos[0]][col + pos[1]]
            if curVal is ".":
                continue
            if curVal in s:
                return False
            s.add(curVal)
        return True

    def validRow(self, board, row):
        s = set()
        for curVal in board[row]:
            if curVal is ".":
                continue
            if curVal in s:
                return False
            s.add(curVal)
        return True

    def validCol(self, board, col):
        s = set()
        for row in board:
            curVal = row[col]
            if curVal is ".":
                continue
            if curVal in s:
                return False
            s.add(curVal)
        return True

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        pos3by3 = [
            [1, 1], [1, 4], [1, 7],
            [4, 1], [4, 4], [4, 7],
            [7, 1], [7, 4], [7, 7]
        ]
        for pos in pos3by3:
            if not self.valid3by3(board, pos[0], pos[1]):
                return False

        for row in range(0, 9):
            if not self.validRow(board, row):
                return False

        for col in range(0, 9):
            if not self.validCol(board, col):
                return False
        return True


s = Solution()
board = [
    [".", "8", "7", "6", "5", "4", "3", "2", "1"],
    ["2", ".", ".", ".", ".", ".", ".", ".", "."],
    ["3", ".", ".", ".", ".", ".", ".", ".", "."],
    ["4", ".", ".", ".", ".", ".", ".", ".", "."],
    ["5", ".", ".", ".", ".", ".", ".", ".", "."],
    ["6", ".", ".", ".", ".", ".", ".", ".", "."],
    ["7", ".", ".", ".", ".", ".", ".", ".", "."],
    ["8", ".", ".", ".", ".", ".", ".", ".", "."],
    ["9", ".", ".", ".", ".", ".", ".", ".", "."]
]
res = s.isValidSudoku(board)
print(res)
