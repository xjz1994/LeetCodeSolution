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

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        for row in board:
            for pos in row:
                print(pos)


board = [
    [".", ".", "9", "7", "4", "8", ".", ".", "."],
    ["7", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", "2", ".", "1", ".", "9", ".", ".", "."],
    [".", ".", "7", ".", ".", ".", "2", "4", "."],
    [".", "6", "4", ".", "1", ".", "5", "9", "."],
    [".", "9", "8", ".", ".", ".", "3", ".", "."],
    [".", ".", ".", "8", ".", "3", ".", "2", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "6"],
    [".", ".", ".", "2", "7", "5", "9", ".", "."]
]
s = Solution()
s.solveSudoku(board)
