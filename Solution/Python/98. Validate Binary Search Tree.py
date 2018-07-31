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
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(node, leftMin, rightMax):
            if node is None:
                return True
            if node.val <= rightMax or node.val >= leftMin:
                return False
            leftRes = helper(node.left, min(node.val, leftMin), rightMax)
            rightRes = helper(node.right, leftMin, max(node.val, rightMax))
            return leftRes and rightRes

        return helper(root, float('inf'), -float('inf'))


root = Tree.CreateTree([5, 1, 4, None, None, 3, 6])
s = Solution()
res = s.isValidBST(root)
print(res)
