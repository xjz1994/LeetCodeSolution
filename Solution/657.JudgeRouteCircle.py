class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        res = [0,0]
        def o(s):
            if s == "L":
                res[0] = res[0] - 1
            elif s == "R":
            elif s == "U":
                res[1] = res[1] + 1
            elif s == "D":

        for i in range(0,len(moves)):
            o(moves[i])
        
        return res[0] == res[1] == 0
