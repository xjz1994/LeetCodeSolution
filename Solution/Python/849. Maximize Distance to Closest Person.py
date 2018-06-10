class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        d = {}
        res = l = left = r = right = 0
        for i, s in enumerate(seats):
            if not s and left:
                d[i] = l = l + 1
            elif s:
                l, left = 0, 1
        for i in range(len(seats) - 1, -1, -1):
            if not seats[i] and right and (i not in d or d[i] > r):
                d[i] = r = r + 1
            elif seats[i]:
                r, right = 0, 1
        return max(d.values())


seats = [1, 0, 0, 0, 1, 0, 1]
res = Solution().maxDistToClosest(seats)
print(res)
