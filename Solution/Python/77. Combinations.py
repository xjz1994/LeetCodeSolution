class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []

        def gen(l, index):
            if len(l) == k:
                res.append(l[:])
                return
            for i in range(index, n + 1):
                gen(l + [i], i + 1)

        gen([], 1)
        return res


s = Solution()
n = 4
k = 2
res = s.combine(n, k)
print(res)
