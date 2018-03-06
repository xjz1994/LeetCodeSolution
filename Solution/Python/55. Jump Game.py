class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        lastPos = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= lastPos:
                lastPos = i
        return lastPos == 0


s = Solution()
nums = [2, 3, 1, 1, 4]
#nums = [3, 2, 1, 0, 4]
res = s.canJump(nums)
print(res)
