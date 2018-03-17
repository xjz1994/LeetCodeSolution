class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        pos = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def check(row, col):
            stack = []
            stack.append([row, col, 0, None, None])
            while stack:
                cur = stack.pop()
                if board[cur[0]][cur[1]] == word[cur[2]]:
                    if cur[2] == len(word) - 1:
                        return True
                    for i in pos:
                        newRow = cur[0] + i[0]
                        newCol = cur[1] + i[1]
                        if newRow >= 0 and newRow < len(board) and newCol >= 0 and newCol < len(board[0]):
                            if newRow != cur[3] and newCol != cur[4]:
                                stack.append(
                                    [newRow, newCol, cur[2] + 1, cur[0], cur[1]])
                            else:
                                print(newRow, ",", newCol)
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if check(i, j):
                    return True
        return False


s = Solution()
board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]
word = "ABCCED"
#word = "SEE"
#word = "ABCB"
res = s.exist(board, word)
print(res)
