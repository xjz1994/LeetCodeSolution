class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res = [0 for i in range(len(A))]
        evenIdx = 0
        oddIdx = 1
        for i in A:
            if i % 2 == 0:
                res[evenIdx] = i
                evenIdx += 2
            else:
                res[oddIdx] = i
                oddIdx += 2
        return res


arr = [4, 2, 5, 7]
res = Solution().sortArrayByParityII(arr)
print(res)
