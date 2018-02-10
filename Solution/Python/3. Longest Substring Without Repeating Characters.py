class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # m = {}
        # repeat = False
        # for i in range(len(s)):
        #     pos = m.get(s[i], [])
        #     pos.append(i)
        #     m[s[i]] = pos
        #     repeat = len(pos) > 1 or repeat

        # if not repeat:
        #     return len(s)

        # res = 0
        # l = []
        # for i in m:
        #     l += m[i]

        # z = zip(l, l[1:])
        # for x, y in z:
        #     print(x, ",", y)
        #     res = max(res, y - x)

        # return res


#s = ""
#s = "a"
#s = "au"
#s = "aabbb"
s = "abcabcbb"
#s = "bbbb"
#s = "pwwkew"
solution = Solution()
res = solution.lengthOfLongestSubstring(s)
print(res)
