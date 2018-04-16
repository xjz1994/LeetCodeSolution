class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        import re

        banSet = set([i.lower() for i in banned])
        words = re.findall(r"\w+", paragraph)
        d = {}
        maxTime = 0
        res = ""
        for i in words:
            cur = i.lower()
            if cur in banSet:
                continue
            d[cur] = d.get(cur, 0) + 1
            if d[cur] > maxTime:
                maxTime = d[cur]
                res = cur

        return res


s = Solution()
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
res = s.mostCommonWord(paragraph, banned)
print(res)
