class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        path = []

        def gen(s, path, res):
            if not s:
                res.append(path)
                return

            for i in range(len(s)):
                if i > 0 and s[i] == s[i - 1]:
                    continue
                gen(s[:i] + s[i + 1:], path + [s[i]], res)

        gen(nums, path, res)
        return res


# nums = [1, 1, 2]
nums = [2, 2, 1, 1]
s = Solution()
res = s.permuteUnique(nums)
print(res)
