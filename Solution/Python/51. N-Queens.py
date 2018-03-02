class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        solutions = []

        def available(queen, row, col):
            for k in range(row):
                if queen[k] is col or abs(queen[k] - col) is abs(k - row):
                    return False
            return True

        def find(queen, row):
            if row == n:
                solutions.append(queen[:])
            else:
                for col in range(n):
                    if available(queen, row, col):
                        queen[row] = col
                        find(queen, row + 1)

        find([-1] * n, 0)

        res = []
        for i in solutions:
            solu = []
            for index in i:
                s = '.' * index + 'Q' + '.' * (n - index - 1)
                solu.append(s)
            res.append(solu)

        return res


s = Solution()
n = 4
res = s.solveNQueens(n)
print(res)
