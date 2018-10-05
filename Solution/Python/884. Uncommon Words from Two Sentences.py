class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        arrA = A.split(" ")
        arrB = B.split(" ")
        m = {}

        for i in arrA:
            m[i] = m.get(i, 0) + 1
        for i in arrB:
            m[i] = m.get(i, 0) + 1

        return [i for i in m if m[i] == 1]


A = "this apple is sweet"
B = "this apple is sour"
res = Solution().uncommonFromSentences(A, B)
print(res)
