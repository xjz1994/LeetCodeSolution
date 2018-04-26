import sys
sys.path.append(r'F:\xjzspace\LeetCodeSolution\Helper\Python')
from Tree import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res = True

        def helper(node, leftMin, rightMax):
            if not node:
                return
            if node.val <= rightMax or node.val >= leftMin:
                nonlocal res
                res = False
            helper(node.left, min(node.val, leftMin), rightMax)
            helper(node.right, leftMin, max(node.val, rightMax))

        helper(root, float('inf'), -float('inf'))
        return res


root = Tree.CreateTree([5, 1, 4, None, None, 3, 6])
s = Solution()
res = s.isValidBST(root)
print(res)
