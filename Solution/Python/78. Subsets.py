class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        def gen(path, index):
            if index == len(nums):
                res.append(path[:])
                return
            gen(path, index + 1)
            path.append(nums[index])
            gen(path, index + 1)
            path.pop()

        gen([], 0)
        return res


s = Solution()
nums = [1, 2, 3]
res = s.subsets(nums)
print(res)
