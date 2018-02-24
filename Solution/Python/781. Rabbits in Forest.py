class Solution:
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        res = 0
        m = {}
        for i in answers:
            if i == 0:
                res += 1
                continue
            if m.get(i) != None:
                m[i] = m[i] + 1
                if m[i] == i:
                    del m[i]
            else:
                m.update({i: 0})
                res += i + 1
        return res


s = Solution()
answers = [1, 1, 2]
#answers = [10, 10, 10]
res = s.numRabbits(answers)
print(res)
