class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []

        def gen(s, path):
            if not s:
                res.append(path)
                return
            for i in range(1, len(s)+1):
                if s[:i] == s[:i][::-1]:
                    gen(s[i:], path+[s[:i]])

        gen(s, [])
        return res


# s = "aab"
s = "aabab"
res = Solution().partition(s)
print(res)
