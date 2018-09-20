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
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        leafs1 = []
        leafs2 = []

        def getLeafs(root, res):
            if root.left == None and root.right == None:
                res.append(root.val)
            else:
                if root.left != None:
                    getLeafs(root.left, res)
                if root.right != None:
                    getLeafs(root.right, res)

        getLeafs(root1, leafs1)
        getLeafs(root2, leafs2)

        return leafs1 == leafs2


root1 = Tree.CreateTree(
    [3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]
)
root2 = Tree.CreateTree(
    [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8]
)

res = Solution().leafSimilar(root1, root2)
print(res)
