class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        B = set()
        for string in A:
            C = list(string)
            a, b = C[::2], C[1::2]
            B.add((''.join(sorted(a)), ''.join(sorted(b))))
        return len(B)


A = ["abc", "acb", "bac", "bca", "cab", "cba"]
res = Solution().numSpecialEquivGroups(A)
print(res)
