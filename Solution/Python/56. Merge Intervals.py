# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        sortedList = sorted(intervals, key=lambda x: (x.start, x.end))
        res = []
        for i in sortedList:
            if not res or res[-1].end < i.start:
                res.append(i)
            else:
                res[-1].end = max(res[-1].end, i.end)
        return res


s = Solution()
intervals = [Interval(1, 3), Interval(2, 6), Interval(15, 18), Interval(8, 10)]
res = s.merge(intervals)
print(res)
