class RecentCounter:

    def __init__(self):
        self.p = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.p.append(t)
        while self.p[0] < t-3000:
            self.p.pop(0)
        return len(self.p)


# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
param_1 = obj.ping(10)
