class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        left = right = 0
        while right < len(A):
            value = A[right]
            if value % 2 == 0:
                A[left], A[right] = A[right], A[left]
                left += 1
            right += 1
        return A


A = [3, 1, 2, 4]
res = Solution().sortArrayByParity(A)
print(A)
