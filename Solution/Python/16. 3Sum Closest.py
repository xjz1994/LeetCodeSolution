class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = sum(nums[0:3])
        for i in range(0, len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == target:
                    return s
                res = s if abs(s - target) < abs(res - target) else res
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
        return res


s = Solution()

nums = [-1, 2, 1, -4]
target = 1

res = s.threeSumClosest(nums, target)
print(res)
