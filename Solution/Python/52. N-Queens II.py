class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        queen = [-1] * n

        def available(queen, row, col):
            for k in range(row):
                if queen[k] is col or abs(queen[k] - col) is abs(k - row):
                    return False
            return True

        def find(queen, row):
            if row == n:
                nonlocal count
                count += 1
            else:
                for col in range(n):
                    if available(queen, row, col):
                        queen[row] = col
                        find(queen, row + 1)

        find([-1] * n, 0)
        return count


s = Solution()
n = 8
res = s.totalNQueens(n)
print(res)
