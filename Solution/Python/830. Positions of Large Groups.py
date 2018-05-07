class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        res = []
        groupStarIndex = 0
        groupEndIndex = 0
        groupSize = 1
        for i in range(len(S)):
            # 字符串结尾或新分组
            if i >= len(S) - 1 or S[i+1] != S[i]:
                if groupSize >= 3:
                    groupEndIndex = i
                    res.append([groupStarIndex, groupEndIndex])
                groupSize = 1
                groupStarIndex = i + 1
                groupEndIndex = i
            else:
                groupSize += 1
        return res


#S = "abbxxxxzzy"
#S = "abc"
S = "abcdddeeeeaabbbcd"
s = Solution()
res = s.largeGroupPositions(S)
print(res)
