class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        m = {}
        for i in range(len(nums)):
            c = nums[i]
            if m.get(target - c) != None:
                return [m[target - c], i]
            else:
                m[c] = i
        return []


s = Solution()

#nums = [3, 2, 4]
#target = 6
nums = [3, 3]
target = 6
res = s.twoSum(nums, target)
print(res)
