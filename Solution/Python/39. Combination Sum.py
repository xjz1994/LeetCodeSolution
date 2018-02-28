class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []

        def gen(nums, remain):
            if remain == 0:
                res.append(nums[:])
                return
            for i in candidates:
                if i > remain:
                    break
                if nums and i < nums[-1]:
                    continue
                gen(nums + [i], remain - i)

        candidates.sort()
        gen([], target)

        return res


s = Solution()
# candidates = [2, 3, 6, 7]
# target = 7
# candidates = [1, 2, 3, 6, 7]
# target = 4
# candidates = [1]
# target = 2
candidates = [8, 7, 4, 3]
target = 11
res = s.combinationSum(candidates, target)
print(res)
