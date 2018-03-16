class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        m = {}
        for i in nums:
            m[i] = m.get(i, 0) + 1

        for i in range(len(nums)):
            color = 0
            if m.get(0, 0):
                color = 0
            elif m.get(1, 0):
                color = 1
            elif m.get(2, 0):
                color = 2
            nums[i] = color
            m[color] -= 1


s = Solution()
nums = [1, 1, 2, 0, 0, 1, 2, 1, 2, 0, 1, 2, 0, 0, 1, 1, 2]
s.sortColors(nums)
print(nums)
