class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        lenA = len(word1)
        lenB = len(word2)
        d = [[0 for i in range(lenB + 1)] for i in range(lenA + 1)]

        for i in range(len(d)):
            d[i][0] = i
        for i in range(len(d[0])):
            d[0][i] = i

        for i in range(1, lenA + 1):
            for j in range(1, lenB + 1):
                if (word1[i - 1] == word2[j - 1]):
                    d[i][j] = d[i - 1][j - 1]
                else:
                    d[i][j] = min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + 1)

        return d[lenA][lenB]


s = Solution()
word1 = "abcde"
word2 = "abcd"
res = s.minDistance(word1, word2)
print(res)
