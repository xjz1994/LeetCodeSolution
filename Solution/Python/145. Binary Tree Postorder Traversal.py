# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def getHelperPath():
    path = __file__.split("\\")[0:-1]
    path[-2] = "Helper"
    return "\\".join(path)


import sys
sys.path.append(getHelperPath())
from Tree import *


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        node = root
        lastVisit = root
        while node or len(stack) != 0:
            while node:
                stack.append(node)
                node = node.left
            node = stack[-1]
            if not node.right or node.right == lastVisit:
                stack.pop()
                res.append(node.val)
                lastVisit = node
                node = None
            else:
                node = node.right
        return res


root = Tree.CreateTree([1, None, 2, 3])
s = Solution()
res = s.postorderTraversal(root)
print(res)
