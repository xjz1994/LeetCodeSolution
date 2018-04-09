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
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def prune(node, parent):
            if not node:
                return
            prune(node.left, node)
            prune(node.right, node)
            if parent and node.val == 0 and not node.left and not node.right:
                if node == parent.left:
                    parent.left = None
                elif node == parent.right:
                    parent.right = None

        prune(root, None)
        return root


s = Solution()
#root = Tree.CreateTree([1, None, 0, 0, 1])
#root = Tree.CreateTree([1, 0, 1, 0, 0, 0, 1])
root = Tree.CreateTree([1, 1, 0, 1, 1, 0, 1, 0])
newRoot = s.pruneTree(root)
Tree.BFSWalk(newRoot, lambda node: print(node.val))
