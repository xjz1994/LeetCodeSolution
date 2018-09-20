def getHelperPath():
    path = __file__.split("\\")[0:-1]
    path[-2] = "Helper"
    return "\\".join(path)


import sys
sys.path.append(getHelperPath())
from Tree import *


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root.val == val:
            return root
        else:
            if root.left != None and val < root.val:
                return self.searchBST(root.left, val)
            elif root.right != None and val > root.val:
                return self.searchBST(root.right, val)
            else:
                return None


root = Tree.CreateTree([4, 2, 7, 1, 3, None, None])
res = Solution().searchBST(root, 3)
print(res)
