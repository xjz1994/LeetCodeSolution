class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res = []
        if len(digits) == 0:
            return res
        for c in digits:
            if not c in "23456789":
                return res

        m = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def gen(i, s):
            if i > len(digits) - 1:
                res.append(s)
                return
            for c in m[digits[i]]:
                gen(i + 1, s + c)

        gen(0, "")

        return res


s = Solution()

digits = "234"

res = s.letterCombinations(digits)
print(res)
