class Solution(object):
    def singleNonDuplicate(self, nums):
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = int((lo + hi) / 2)
            if nums[mid] == nums[mid ^ 1]:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mi = (lo + hi) >> 1
            if nums[mi] == nums[mi - 1]:
                if (mi - 1) &amp; 1:
                    hi = mi - 2
                else:
                    lo = mi + 1
            elif nums[mi] == nums[mi + 1]:
                if (mi + 1) &amp; 1:
                    lo = mi + 2
                else:
                    hi = mi - 1
            else:
                return nums[mi]
        return nums[lo]
