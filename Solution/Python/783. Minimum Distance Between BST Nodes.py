import sys
sys.path.append(r'F:\xjzspace\LeetCodeSolution\Helper\Python')
from BSTree import *
from Tree import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = float('inf')
        pre = -float('inf')

        def find(root):
            nonlocal res
            nonlocal pre
            if root.left:
                find(root.left)
            res = min(res, root.val - pre)
            pre = root.val
            if root.right:
                find(root.right)

        find(root)
        return res


#root = BSTree.CreateBSTree(4, [2, 6, 1, 3, None, None])
#root = BSTree.CreateBSTree(90, [69, None, 49, 89, None, 52])
#root = BSTree.CreateBSTree(1, [0, 48, None, None, 12, 49])
root = BSTree.CreateBSTree(956, [267, 961, 7, 296, None, 981, None, 138, None, 496, None, None, None, 263, 362, 638, None, None,
                                 308, 409, None, 703, None, 322, None, None, None, 769, None, None, None, 883, 808, 945, None, None, 915, None, None, None])
# Tree.InOrderWalk(root, lambda node: print(node.val))
s = Solution()
res = s.minDiffInBST(root)
print(res)
