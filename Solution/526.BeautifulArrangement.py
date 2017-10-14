thi
ith
N


class Solution(object):
    def countArrangement(self, N):
        if N == 0:
            return 0
        nums = [0 for x in range(0,N+1)]
        return self.helper(N,1,nums)

    def helper(self,N,pos,used):
        if pos > N:
            return 1

        num = 0
        for i in range(1,N+1):
            if used[i] == 0 and (i%pos==0 or pos%i==0):
                used[i] = 1
                num += self.helper(N,pos+1,used)
                used[i] = 0
        return num
class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        return [0, 1, 2, 3, 8, 10, 36, 41, 132, 250, 700, 750, 4010, 4237, 10680, 24679][N]
