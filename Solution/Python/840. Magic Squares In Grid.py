class Solution:
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def check(x, y):
            g = grid
            a = g[y-1][x-1] + g[y][x-1] + g[y+1][x-1]
            b = g[y-1][x+1] + g[y][x+1] + g[y+1][x+1]
            c = g[y-1][x-1] + g[y-1][x] + g[y-1][x+1]
            d = g[y+1][x-1] + g[y+1][x] + g[y+1][]
            e = g[y-1][x-1] + g[y][x] + g[y+1][x+1]
            f = g[y-1][x+1] + g[y][x] + g[y+1][x-1]
            return a == 15 and b == 15 and c == 15 and d == 15 and e == 15

        res = 0

        startX = min(len(grid[0]), 1)
        endX = max(len(grid[0]) - 2, 0)
        startY = min(len(grid), 1)
        endY = max(len(grid) - 2, 0)

        for x in range(startX, endX + 1):
            for y in range(startY, endY + 1):
                if(check(x, y)):
                    res += 1

        return res


# grid = [[4, 3, 8, 4],
#         [9, 5, 1, 9],
#         [2, 7, 6, 2]]

grid = [[1, 8, 6],
        [10, 5, 0],
        [4, 2, 9]]
res = Solution().numMagicSquaresInside(grid)
print(res)
