class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        res = [[i ^ 1 for i in row[::-1]] for row in A]
        return res


A = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
res = Solution().flipAndInvertImage(A)
print(res)
