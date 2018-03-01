class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        used = []

        def count(l):
            m = {}
            for i in l:
                m[i] = m.get(i, 0) + 1
            return m

        def gen(nums, remain, index):
            if remain < 0:
                return
            if remain == 0:
                m = count(nums)
                if m not in used:
                    used.append(m)
                    res.append(nums[:])
                return
            for i in range(index, len(candidates)):
                cur = candidates[i]
                gen(nums + [cur], remain - cur, i + 1)

        gen([], target, 0)

        return res


s = Solution()
# candidates = [1, 1, 2, 3]
# target = 3
# candidates = [10, 1, 2, 7, 6, 1, 5]
# target = 8
candidates = [2, 5, 1, 1, 2, 3, 3, 3, 1, 2, 2]
target = 5
res = s.combinationSum2(candidates, target)
print(res)
