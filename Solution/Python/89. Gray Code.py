class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n < 1:
            return [0]
        if (n == 1):
            return [0, 1]

        res = self.grayCode(n - 1)
        x = pow(2, n - 1)
        for i in range(x - 1, -1, -1):
            res.append(res[i] + x)
        return res


s = Solution()
n = 3
res = s.grayCode(n)
print(res)
