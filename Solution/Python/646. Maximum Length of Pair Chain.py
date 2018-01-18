class Solution:
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        res = 0
        sortedPairs = sorted(pairs, key=lambda x: (x[0], x[1]))
        pre = -2147483648
        for pair in sortedPairs:
            if pre < pair[0]:
                res += 1
                pre = pair[1]
            elif pair[1] < pre:
                pre = pair[1]
        return res


#pairs = [[1, 2], [2, 3], [5, 2], [3, 4], [3, 10]]
pairs = [[-6, 9], [1, 6], [8, 10], [-1, 4], [-6, -2], [-9, 8], [-5, 3], [0, 3]]
s = Solution()
res = s.findLongestChain(pairs)
print(res)
