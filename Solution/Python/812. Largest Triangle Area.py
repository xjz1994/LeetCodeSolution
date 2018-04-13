class Solution:
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        res = 0
        n = len(points)
        for p1 in range(n - 2):
            for p2 in range(p1 + 1, n - 1):
                for p3 in range(p2 + 1, n):
                    x1, y1 = points[p1]
                    x2, y2 = points[p2]
                    x3, y3 = points[p3]
                    area = abs(x1 * (y2 - y3)
                               + x2 * (y3 - y1)
                               + x3 * (y1 - y2)) * 0.5
                    res = max(res, area)
        return res


s = Solution()
points = [[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]
res = s.largestTriangleArea(points)
print(res)
