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
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if(not root):
            return []
        res = []

        stack = []
        current = root
        while(current != None):
            stack.append(current)
            current = current.left
        while(stack):
            current = stack.pop()
            res.append(current.val)
            node = current.right
            while(node != None):
                stack.append(node)
                node = node.left

        return res


root = Tree.CreateTree([1, None, 2, 3])
s = Solution()
res = s.inorderTraversal(root)
print(res)
