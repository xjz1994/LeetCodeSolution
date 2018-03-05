class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        import copy
        m = copy.deepcopy(matrix)
        res = []
        while(m and m[0]):
            if len(m) == 1:
                res += m[0]
                break

            # 顶
            res += m[0][:]
            # 右
            if len(m) > 2:
                res += [m[i][-1] for i in range(1, len(m) - 1)]
            # 底
            res += m[-1][::-1]
            # 左
            if len(m) > 2 and len(m[-1]) > 1:
                res += [m[i][0] for i in range(1, len(m) - 1)][::-1]

            # 移除本轮循环已加入的元素
            if len(m) > 2:
                for i in range(1, len(m) - 1):
                    if m[i]:
                        m[i].pop()
                    if m[i]:
                        m[i].pop(0)
            m.pop(0)
            m.pop()

        return res


s = Solution()
# matrix = [
#     [5]
# ]
# matrix = [
#     [1, 2],
#     [3, 4]
# ]
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# matrix = [
#     [1, 2, 3, 4],
#     [4, 5, 6, 7],
#     [7, 8, 9, 10],
#     [11, 12, 13, 14]
# ]
# matrix = [
#     [7],
#     [9],
#     [6]
# ]
# matrix = [
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10],
#     [11, 12, 13, 14, 15],
#     [16, 17, 18, 19, 20],
#     [21, 22, 23, 24, 25]
# ]
# matrix = [
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10],
#     [11, 12, 13, 14, 15],
#     [16, 17, 18, 19, 20],
#     [21, 22, 23, 24, 25]
# ]
res = s.spiralOrder(matrix)
print(res)
