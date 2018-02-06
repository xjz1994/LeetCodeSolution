class Solution:
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        used = [False for x in range(10)]

        def gen(used, n, d):
            if n == d:
                return 1
            total = 1
            startIndex = 1 if d == 0 else 0
            for i in range(startIndex, 10):
                if not used[i]:
                    used[i] = True
                    total += gen(used, n, d + 1)
                    used[i] = False
            return total

        return gen(used, n, 0)


s = Solution()
a = s.countNumbersWithUniqueDigits(7)
print(a)
