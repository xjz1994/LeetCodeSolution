class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        x = "{0:b}".format(N)

        if x.count('1') <= 1:
            return 0

        gap = 0
        last = 0
        for v, num in enumerate(x):
            if num == '1':
                gap = max(v - last, gap)
                last = v
            else:
                continue

        return gap


N = 22
res = Solution().binaryGap(N)
print(res)
