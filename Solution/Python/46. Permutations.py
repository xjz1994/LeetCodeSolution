class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        s = set(nums)

        def gen(l):
            if len(l) is len(nums):
                res.append(l[:])
            else:
                for i in s:
                    if not i in l:
                        l.append(i)
                        gen(l)
                        l.pop()

        gen([])
        return res


nums = [1, 2, 3]
s = Solution()
res = s.permute(nums)
print(res)
