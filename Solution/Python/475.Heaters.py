class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        res = 0
        j = 0
        for i in range(0, len(houses)):
            while j < len(heaters) - 1 and abs(heaters[j + 1] - houses[i]) <= abs(heaters[j] - houses[i]):
                j += 1
            res = max(res, abs(heaters[j] - houses[i]))
        return res
