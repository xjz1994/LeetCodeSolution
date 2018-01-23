class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []

        def gen(s="", open=0, close=0):
            if len(s) is 2 * n:
                res.append(s)
            else:
                if open < n:
                    gen(s + "(", open + 1, close)
                if close < open:
                    gen(s + ")", open, close + 1)

        gen()
        return res


n = 3
s = Solution()
res = s.generateParenthesis(3)
print(res)
