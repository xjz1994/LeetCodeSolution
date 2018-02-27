class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        a = self.majorityElement(nums[:len(nums) // 2])
        b = self.majorityElement(nums[len(nums) // 2:])
        if a == b:
            return a
        return [b, a][nums.count(a) > len(nums) // 2]


s = Solution()
nums = [7, 7, 5, 7, 5, 1, 5, 7, 5, 5, 7, 7, 7, 7, 7, 7]
res = s.majorityElement(nums)
print(res)
