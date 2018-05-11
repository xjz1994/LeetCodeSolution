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
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        def dfs(root, sum):
            if root == None:
                return False
            if root.left == None and root.right == None and sum == root.val:
                return True
            return dfs(root.left, sum - root.val) or dfs(root.right, sum - root.val)

        return dfs(root, sum)


root = Tree.CreateTree([5, 4, 8, 11, 3, 4, 7, 2, None, None, 1])
s = Solution()
res = s.hasPathSum(root, 22)
print(res)
