class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        s = set(nums)

        def gen(l, added):
            if len(l) is len(nums):
                res.append(l[:])
            else:
                for i in s:
                    if not i in added:
                        gen(l + [i], set(l + [i]))

        gen([], set())
        return res


nums = [1, 2, 3, 4, 5]
s = Solution()
res = s.permute(nums)
print(res)
