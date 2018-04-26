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
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if root is None:
            return res

        queue = [root]
        isReverse = 0
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
                isReverse = isReverse ^ 1
                level = level[::-1] if isReverse else level
                res.append(level)

        return res


root = Tree.CreateTree([3, 9, 20, None, None, 15, 7])
s = Solution()
res = s.zigzagLevelOrder(root)
print(res)
