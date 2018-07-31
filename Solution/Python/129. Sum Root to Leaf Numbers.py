def getHelperPath():
    path = __file__.split("\\")[0:-1]
    path[-2] = "Helper"
    return "\\".join(path)


import sys
sys.path.append(getHelperPath()))
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
        paths=[]

        def dfs(node, path):
            if not node:
                return
            if node.left == None and node.right == None:
                path += str(node.val)
                paths.append(path)
            if node.left:
                dfs(node.left, path + str(node.val))
            if node.right:
                dfs(node.right, path + str(node.val))

        dfs(root, "")
        l=[int(i) for i in paths]
        return sum(l)


# root = Tree.CreateTree([4, 9, 0, 5, 1])
root=Tree.CreateTree([])
res=Solution().sumNumbers(root)
print(res)
