import sys
sys.path.append(r'F:\xjzspace\space\LeetCodeSolution\Helper\Python')
from Tree import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if root is None:
            return res

        queue = [root]
        while queue and queue[0]:
            level = []
            count = len(queue)
            for i in range(count):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if level:
                res.append(level)
        return res[::-1]


root = Tree.CreateTree([3, 9, 20, None, None, 15, 7])
s = Solution()
res = s.levelOrderBottom(root)
print(res)
