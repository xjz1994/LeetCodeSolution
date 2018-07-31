def getHelperPath():
    path = __file__.split("\\")[0:-1]
    path[-2] = "Helper"
    return "\\".join(path)


import sys
sys.path.append(getHelperPath())
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

        def gen(path, node, sum):
            if node == None:
                return
            if node.left == None and node.right == None:
                if sum - node.val == 0:
                    res.append(path + [node.val][::])
            if node.left:
                gen(path + [node.val], node.left, sum - node.val)
            if node.right:
                gen(path + [node.val], node.right, sum - node.val)

        gen([], root, sum)
        return res


root = Tree.CreateTree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
res = Solution().pathSum(root, 22)
print(res)
