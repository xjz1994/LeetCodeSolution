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
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        paths = []

        def dfs(node, path):
            if node.left == None and node.right == None:
                paths.append(path)
            if node.left:
                dfs(node.left, path + str(node.val))
            if node.right:
                dfs(node.right, path + str(node.val))

        dfs(root, "")
        print(paths)


root = Tree.CreateTree([4, 9, 0, 5, 1])
res = Solution().sumNumbers(root)
