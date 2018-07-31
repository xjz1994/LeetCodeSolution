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

# 使用迭代，对二叉树进行先序遍历
class Solution1:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                res.append(node.val)
                node = node.left
            if stack:
                node = stack.pop().right
        return res


class Solution2:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = [root]
        while stack and stack[0]:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res


root = Tree.CreateTree([1, None, 2, 3])
s = Solution()
res = s.preorderTraversal(root)
print(res)
