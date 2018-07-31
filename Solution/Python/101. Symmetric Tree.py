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
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        queue = [root]
        while queue and queue[0]:
            level = []
            count = len(queue)
            for i in range(count):
                node = queue.pop(0)

                if node.left:
                    queue.append(node.left)
                    level.append(node.left.val)
                else:
                    level.append(None)

                if node.right:
                    queue.append(node.right)
                    level.append(node.right.val)
                else:
                    level.append(None)

            if level != level[::-1]:
                return False

        return True


root = Tree.CreateTree([1, 2, 2, 3, 4, 4, 3])
s = Solution()
res = s.isSymmetric(root)
print(res)
