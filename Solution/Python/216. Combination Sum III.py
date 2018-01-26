class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        def gen(l, k, n, start):
            if k == len(l) and n == 0:
                res.append(l[:])
                return
            for i in range(start, 10):
                l.append(i)
                gen(l, k, n - i, i + 1)
                l.pop()
                
        gen([], k, n, 1)
        return res


s = Solution()
res = s.combinationSum3(3, 7)
print(res)