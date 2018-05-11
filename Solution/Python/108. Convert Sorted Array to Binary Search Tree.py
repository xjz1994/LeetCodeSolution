import sys
sys.path.append(
    r'F:\xjzspace\space\LeetCodeSolution\Helper\Python')
from Tree import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None

        def insert(nums, l, r):
            m = (l+r) // 2
            newNode = TreeNode(nums[m])
            if l < m:
                newNode.left = insert(nums, l, m-1)
            if r > m:
                newNode.right = insert(nums, m+1, r)
            return newNode

        return insert(nums, 0, len(nums)-1)


s = Solution()
#nums = []
nums = [-10, -3, 0, 5, 9]
root = s.sortedArrayToBST(nums)
res = Tree.Tree2Array(root)
print(res)
