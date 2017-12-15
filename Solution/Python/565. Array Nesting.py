class Solution:
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen, res = [0] * len(nums), 0
        for i in nums:
            count, j = 0, i
            while not seen[j]:
                seen[j], count, j = 1, count + 1, nums[j]
            res = max(res, count)
        return res


s = Solution()
# res = s.arrayNesting([5, 4, 0, 3, 1, 6, 2])
res = s.arrayNesting([1, 0, 5, 4, 0, 3, 1, 6, 2])
print(res)
