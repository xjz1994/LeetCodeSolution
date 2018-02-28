class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        used = []

        def gen(nums, remain, index):
            if remain < 0:
                return
            if remain == 0:
                s = set(nums)
                if s not in used:
                    used.append(s)
                    res.append(nums[:])
                return
            for i in range(index, len(candidates)):
                cur = candidates[i]
                gen(nums + [cur], remain - cur, i + 1)

        gen([], target, 0)

        return res


s = Solution()
candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
res = s.combinationSum2(candidates, target)
print(res)
