class Solution1(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        bins = []
        for num in nums:
            bins.append('{0:b}'.format(num).zfill(32))

        for i in range(32):
            bitCount = 0
            # zeroCount
            for num in bins:
                if num[i] is '1':
                    bitCount += 1
            # zeroCount = (len(nums) - bitCount)
            res += bitCount * (len(nums) - bitCount)
        return res


class Solution2(object):
    def totalHammingDistance(self, nums):
        res = 0
        for i in range(32):
            bitCount = 0
            for num in nums:
                bitCount += num >> i & 1
            res += bitCount * (len(nums) - bitCount)
        return res


nums = [4, 14, 2]
s = Solution1()
res = s.totalHammingDistance(nums)
print(res)
