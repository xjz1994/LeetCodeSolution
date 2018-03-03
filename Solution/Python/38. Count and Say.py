class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = "1"
        for _ in range(n - 1):
            res = self.helper(res)
        return res

    def helper(self, n):
        count, i, res = 1, 0, ""
        while i < len(n) - 1:
            if n[i] == n[i + 1]:
                count += 1
            else:
                res += str(count) + n[i]
                count = 1
            i += 1
        res += str(count) + n[i]
        return res


s = Solution()
n = 4
res = s.countAndSay(n)
print(res)
