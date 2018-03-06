class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[]] * n
        num = 1
        loop = 0
        while num <= n * n:
            # 顶
            row = res[loop]
            add = []
            for i in range(0, n - (2 * loop)):
                add += [num]
                num += 1
            res[loop] = row[0:loop] + add + row[loop:]

            if num > n * n:
                break

            # 右
            for i in range(loop + 1, n - loop - 1):
                res[i] = res[i][0:loop] + [num] + res[i][loop:]
                num += 1

            # 底
            row = res[-(loop + 1)]
            add = []
            for i in range(0, n - (2 * loop)):
                add = [num] + add
                num += 1
            res[-(loop + 1)] = row[0:loop] + add + row[loop:]

            # 左
            for i in range(n - loop - 2, loop, -1):
                res[i] = res[i][0:loop] + [num] + res[i][loop:]
                num += 1

            loop += 1
        return res


matrix = [
    [1,   2,  3,  4, 5],
    [16, 17, 18, 19, 6],
    [15, 24, 25, 20, 7],
    [14, 23, 22, 21, 8],
    [13, 12, 11, 10, 9]
]
s = Solution()
res = s.generateMatrix(4)
print(res)
