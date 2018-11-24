class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            idx = (left + right)//2
            if nums[idx] < target:
                left = idx + 1
            elif nums[idx] > target:
                right = idx - 1
            else:
                return idx
        return -1


nums = [-1, 0, 3, 5, 9, 12]
target = -1
res = Solution().search(nums, target)
print(res)
