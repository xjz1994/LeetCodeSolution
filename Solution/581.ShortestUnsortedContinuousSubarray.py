
<=
class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        copyNums = nums[::]
        copyNums.sort()
        left = len(nums) - 1
        right = len(nums) - 1
        for i in range(0, len(nums)):
            if nums[i] != copyNums[i]:
                left = i
                break

        for i in range(len(nums) - 1, 0, -1):
            if nums[i] != copyNums[i]:
                right = i
                break

        if right - left == 0:
            return 0
        else:
            return (right - left) + 1
