class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        res = 0
        s = set([(i) for i in J])        
        for i in S:
            if i in s:
                res+=1
        return res
        

J = "aaAA"
S = "aAAbbbb"
s = Solution()
res = s.numJewelsInStones(J,S)
print(res)
