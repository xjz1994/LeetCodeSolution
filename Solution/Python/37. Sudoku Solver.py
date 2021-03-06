class Solution:
    def validPos(self, board, row, col, c):
        x = 3 * int(row / 3)    # 3*3 start x index
        y = 3 * int(col / 3)    # 3*3 start y index
        for i in range(9):
            if board[row][i] == c:
                return False
            if board[i][col] == c:
                return False
            if board[x + int(i / 3)][y + i % 3] == c:
                return False
        return True

    def solve(self, board, solved):
        while solved != 81 and board[int(solved / 9)][solved % 9] != ".":
            solved += 1
        if solved is 81:
            return True

        i = int(solved / 9)
        j = solved % 9
        for c in "123456789":
            if self.validPos(board, i, j, c):
                board[i][j] = c
                if self.solve(board, solved):
                    return True
                else:
                    board[i][j] = "."
        return False

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.solve(board)


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
