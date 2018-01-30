import sys
sys.path.append(r'F:\xjzspace\LeetCodeSolution\Helper\Python')
from Tree import *


class Solution:
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d is 1:
            newRoot = TreeNode(v)
            newRoot.left = root
            return newRoot

        queue = [root]
        while queue and d > 2:
            d -= 1
            count = len(queue)
            for i in range(count):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        for curNode in queue:
            temp = curNode.left
            curNode.left = TreeNode(v)
            curNode.left.left = temp
            temp = curNode.right
            curNode.right = TreeNode(v)
            curNode.right.right = temp
        return root


root = Tree.CreateTree([4, 2, 6, 3, 1, 5])
# print(Tree.Tree2Arr(root))
s = Solution()
v = 1
d = 3
newRoot = s.addOneRow(root, v, d)
print(Tree.Tree2Array(newRoot))
