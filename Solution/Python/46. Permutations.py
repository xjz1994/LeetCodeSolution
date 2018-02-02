import time


class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        s = set(nums)

        def gen(l):
            if len(l) is len(nums):
                res.append(l[:])
            else:
                for i in s:
                    if not i in l:
                        l.append(i)
                        gen(l)
                        l.pop()

        gen([])
        return res


class Solution2:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        s = set(nums)

        def gen(l, added):  # 加入一个set，存储已经在list中的元素，len(nums) > 8时，性能有明显提升
            if len(l) is len(nums):
                res.append(l[:])
            else:
                for i in s:
                    if not i in added:
                        l.append(i)
                        added.add(i)
                        gen(l, added)
                        l.pop()
                        added.remove(i)

        gen([], set())
        return res


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
s = Solution()
start = time.clock()
res = s.permute(nums)
print(time.clock() - start)
