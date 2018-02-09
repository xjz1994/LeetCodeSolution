class Solution:
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        def convert(time):
            return int(time[:2]) * 60 + int(time[3:])

        minutes = [convert(i) for i in timePoints]
        minutes.sort()

        z = zip(minutes, minutes[1:] + minutes[:1])
        return min([(y - x) % (24 * 60) for x, y in z])


s = Solution()
timePoints = ["23:00", "00:00", "12:00", "23:30", "12:15"]
res = s.findMinDifference(timePoints)
print(res)
