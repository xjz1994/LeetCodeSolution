class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        newNums = nums[len(nums)-k:] + nums[:len(nums)-k]
        for i in range(0,len(nums)):
            nums[i] = newNums[i]
