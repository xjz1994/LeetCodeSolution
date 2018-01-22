class Solution:
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        head = self.buildTrie(nums)
        maxXor = 0
        for num in nums:
            node = head
            curXor = 0
            for bit in range(31, -1, -1):
                chd = int(bool(num & (1 << bit)))
                if node[1 ^ chd]:
                    curXor |= 1 << bit
                    node = node[1 ^ chd]
                else:
                    node = node[chd]
            maxXor = max(maxXor, curXor)
        return maxXor

    def buildTrie(self, nums):
        root = [None, None]
        for num in nums:
            cur = '{0:b}'.format(num).zfill(32)
            node = root
            for i in cur:
                bit = int(i)
                if not node[bit]:
                    node[bit] = [None, None]
                node = node[bit]
        return root


nums = [3, 10, 5, 25, 2, 8]
s = Solution()
res = s.findMaximumXOR(nums)
print(res)
