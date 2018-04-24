class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        pos = []
        for i in range(len(S)):
            if S[i] == C:
                pos.append(i)

        res = [0] * len(S)
        idx = 0
        for i in range(len(S)):
            if S[i] == C and idx < len(pos) - 1:
                idx += 1
            else:
                p = []
                p.append(abs(pos[idx] - i))
                if idx > 0:
                    p.append(abs(pos[idx - 1] - i))
                if idx < len(pos) - 1:
                    p.append(abs(pos[idx + 1] - i))
                res[i] = min(p)

        return res


# S = "loveleetcode"
# C = 'e'

S = "lovletcod"
C = 'e'
solution = Solution()
res = solution.shortestToChar(S, C)
print(res)
