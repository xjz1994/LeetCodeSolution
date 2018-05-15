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
    def flatten(self, root):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root == None:
            return None

        nodes = []

        def preOrder(node):
            nodes.append(node)
            if node.left:
                preOrder(node.left)
            if node.right:
                preOrder(node.right)

        preOrder(root)

        for i in range(len(nodes)):
            nodes[i].left = None
            if i != len(nodes) - 1:
                nodes[i].right = nodes[i+1]
            else:
                nodes[i].right = None


root = Tree.CreateTree([1, 2, 5, 3, 4, None, 6])
Solution().flatten(root)
