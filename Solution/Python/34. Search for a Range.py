class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = [-1, -1]
        if not nums:
            return res

        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid

        if nums[low] != target:
            return res

        res[0] = low

        high = len(nums) - 1
        while low < high:
            mid = (low + high + 1) // 2
            if nums[mid] > target:
                high = mid - 1
            else:
                low = mid

        res[1] = low
        return res


s = Solution()
nums = [5, 7, 7, 8, 8, 10]
target = 8
res = s.searchRange(nums, target)
print(res)
