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
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        arr = []

        def walk(node):
            if node.left:
                walk(node.left)
            arr.append(node)
            if node.right:
                walk(node.right)

        walk(root)

        for i in range(len(arr)):
            arr[i].left = None
            if i < len(arr) - 1:
                arr[i].right = arr[i + 1]
            else:
                arr[i].right = None

        return arr[0]


root = Tree.CreateTree(
    [5, 3, 6, 2, 4, None, 8, 1, None, None, None, 7, 9])
res = Solution().increasingBST(root)
print(res)
