import random


class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.origin = nums[:]
        self.list = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.list = self.origin[:]
        return self.origin

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        random.shuffle(self.list)
        return self.list


# Your Solution object will be instantiated and called as such:
nums = [1, 2, 3, 4, 5]
obj = Solution(nums)
param_0 = obj.shuffle()
param_1 = obj.reset()
param_2 = obj.shuffle()

print(param_0)
print(param_1)
print(param_2)
