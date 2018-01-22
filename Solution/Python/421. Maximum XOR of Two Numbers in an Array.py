class Solution:
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        root = self.buildTrie(nums)
        for num in nums:
            cur = '{0:b}'.format(num).zfill(32)
            node = root
            curValue = ""
            for i in range(len(cur) - 1, -1, -1):
                bit = int(cur[i])
                curValue = str(bit) + curValue
                if node[1 ^ bit]:
                    node = node[1 ^ bit]
                else:
                    node = node[bit]
            res = max(res, curValue)
        return res

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
