# dp
class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0] * (num + 1)

        pow2 = 2
        before = 1
        for i in range(1, num + 1):
            if i == pow2:
                res[i] = 1
                before = 1
                pow2 *= 2
            else:
                res[i] = res[before] + 1
                before += 1

        return res


s = Solution()
num = 8
res = s.countBits(num)
print(res)
