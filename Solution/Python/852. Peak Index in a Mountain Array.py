class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        return A.index(max(A))


A = [0, 2, 1, 0]
res = Solution().peakIndexInMountainArray(A)
print(res)
