class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = []

        def gen(i, s):
            if i == len(S):
                res.append(s)
                return
            if not S[i] in "0123456789":
                gen(i + 1, s + S[i].lower())
                gen(i + 1, s + S[i].upper())
            else:
                gen(i + 1, s + S[i])

        gen(0, "")
        return res


s = Solution()

S = "a1b2"

res = s.letterCasePermutation(S)
print(res)
