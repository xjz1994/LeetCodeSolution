class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        m = {}
        for i in strs:
            s = "".join(sorted(i))
            if m.get(s):
                m[s].append(i)
            else:
                m[s] = [i]

        # return [i for i in m.values()]

        res = []
        for i in m.values():
            res.append(i)
        return res


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
s = Solution()
res = s.groupAnagrams(strs)
print(res)
