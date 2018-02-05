class Solution:
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        used = [False for x in range(10)]

        def gen(used, n, num):
            if n == 0:
                print(num)
                return
            else:
                for i in range(len(used)):
                    if not used[i]:
                        num += str(i)
                        used[i] = True
                        gen(used, n - 1, num)
                        used[i] = False

        gen(used, n, "")
        return res


s = Solution()
a = s.countNumbersWithUniqueDigits(2)
print(a)
