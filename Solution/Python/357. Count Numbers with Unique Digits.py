class Solution:
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0

        def gen(s, n):
            if n == 0:
                nonlocal res
                res += 1
                return
            else:
                for i in "0123456789":
                    if i is '0' or i not in s:
                        gen(s + i, n - 1)

        gen("", n)
        return res


s = Solution()
a = s.countNumbersWithUniqueDigits(3)
print(a)
