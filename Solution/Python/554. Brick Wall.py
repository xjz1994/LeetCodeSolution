class Solution:
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        # 穿过最少的砖块数，即：砖块行数 - 最大的缝隙数量
        # 保存每两块砖之间缝隙的Index，找出缝隙数量最多的Index
        m = {}
        maxGap = 0
        for row in wall:
            gapIndex = 0
            for i in range(0, max(0, len(row) - 1)):
                gapIndex += row[i]
                if gapIndex in m.keys():
                    num = m[gapIndex] + 1
                else:
                    num = 1
                maxGap = max(maxGap, num)
                m.update({gapIndex: num})

        return len(wall) - maxGap


wall = [
    [1, 2, 2, 1],
    [3, 1, 2],
    [1, 3, 2],
    [2, 4],
    [3, 1, 2],
    [1, 3, 1, 1]
]

s = Solution()
res = s.leastBricks(wall)
print(res)
