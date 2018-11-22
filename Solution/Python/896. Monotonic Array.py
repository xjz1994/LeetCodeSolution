class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) <= 2:
            return True

        isIncres = True
        isDecres = True
        for i in range(1, len(A)):
            if A[i] < A[i-1]:
                isIncres = False
            if A[i] > A[i-1]:
                isDecres = False
        return isIncres or isDecres


# arr = [1, 2, 2, 3]
# arr = [6, 5, 4, 4]
# arr = [1, 3, 1]
# arr = [1, 1]
res = Solution().isMonotonic(arr)
print(res)
