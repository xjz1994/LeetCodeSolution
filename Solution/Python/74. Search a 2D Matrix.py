class Solution:
    # 两次二分查找
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        l = 0
        r = len(matrix) - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[m][-1] < target:
                l = m + 1
            else:
                r = m - 1

        targetRow = matrix[l]
        l = 0
        r = len(targetRow) - 1
        while l <= r:
            m = (l + r) // 2
            if targetRow[m] == target:
                return True
            if targetRow[m] > target:
                r = m - 1
            else:
                l = m + 1

        return False


class Solution2:
    # 一次二分查找
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n = len(matrix[0])
        lo, hi = 0, len(matrix) * n
        while lo < hi:
            mid = (lo + hi) / 2
            x = matrix[mid / n][mid % n]
            if x < target:
                lo = mid + 1
            elif x > target:
                hi = mid
            else:
                return True
        return False


s = Solution()
# matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
# target = 20

# matrix = [[1]]
# target = 0

# matrix = [[1], [3]]
# target = 0

matrix = [[]]
target = 0

res = s.searchMatrix(matrix, target)
print(res)
