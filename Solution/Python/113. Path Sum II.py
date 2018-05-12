import sys
sys.path.append(
    r'C:\Users\xjz\Documents\GitHub\LeetCodeSolution\Helper\Python')
from Tree import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []

        def gen(path, node):
            if node.left:
                gen(path + [node.val], node.left)
            if node.right:
                gen(path + [node.val], node.right)
            if node.left == None and node.right == None:
                res.append(path[::])

        # gen()


root = Tree.CreateTree([5, 4, 8, 11, 3, 4, 7, 2, None, None, 1])
res = Solution().pathSum(root)
print(res)
