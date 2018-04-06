class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        rowMax = []
        colMax = []
        for i in grid:
            rowMax.append(max(i))
        for i in range(len(grid[0])):
            colMax.append(max([grid[j][i] for j in range(len(grid[i]))]))
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                res += min(rowMax[i],colMax[j]) - grid[i][j]

        return res


s = Solution()
grid = [
    [3, 0, 8, 4],
    [2, 4, 5, 7],
    [9, 2, 6, 3],
    [0, 3, 1, 0]
]
res = s.maxIncreaseKeepingSkyline(grid)
print(res)

