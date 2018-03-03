class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
        return l


s = Solution()
nums = [1, 3, 5, 6]
target = 7
res = s.searchInsert(nums, target)
print(res)
