class Solution:
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        root = dict()
        leaves = []
        for word in set(words):
            cur = root
            for i in word[::-1]:
                cur[i] = cur = cur.get(i, dict())
            leaves.append((cur, len(word)))

        res = 0
        for node, depth in leaves:
            if len(node) == 0:
                res += depth + 1

        return res


words = ["time", "me", "bell"]
#words = ["time", "atime", "btime"]
s = Solution()
res = s.minimumLengthEncoding(words)
print(res)
