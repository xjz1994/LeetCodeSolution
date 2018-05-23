class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        return rec1[0] < rec2[2] and rec2[0] < rec1[2] and rec1[1] < rec2[3] and rec2[1] < rec1[3]


rec1 = [0, 0, 2, 2]
rec2 = [1, 1, 3, 3]
# rec1 = [0, 0, 1, 1]
# rec2 = [1, 0, 2, 1]
res = Solution().isRectangleOverlap(rec1, rec2)
print(res)
