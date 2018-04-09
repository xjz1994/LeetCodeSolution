class Solution:
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """


s = Solution()
points = [[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]
res = s.largestTriangleArea(points)
print(res)
