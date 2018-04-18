class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []

        def gen(index, path):
            res.append(path[:])
            if index > len(nums):
                return
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i - 1]:
                    continue
                gen(i + 1, path + [nums[i]])

        gen(0, [])
        return res


s = Solution()
nums = [1, 2, 2]
res = s.subsetsWithDup(nums)
print(res)
