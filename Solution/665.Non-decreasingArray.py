class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        times = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                times += 1
                if times == 2:
                    return False
                #[3, 4, 2, 3]
                if (i != 1 and i != len(nums) - 1):
                    if (nums[i - 1] > nums[i + 1] and nums[i] < nums[i - 2]):
                        return False
        return True
