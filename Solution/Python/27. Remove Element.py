class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = len(nums)
        index = 0
        for i in range(0, len(nums)):
            if nums[i] == val:
                length -= 1
            else:
                nums[index] = nums[i]
                index += 1
        return length


s = Solution()

nums = [3, 2, 2, 3]
val = 3
res = s.removeElement(nums, val)
print(res)
