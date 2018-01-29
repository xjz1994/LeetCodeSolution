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
        maxDepth = 0
        queue = [root]
        while queue and queue[0]:
            maxDepth += 1
            count = len(queue)
            for i in range(count):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        depth = 1
        queue = [root]
        while queue and queue[0]:
            depth += 1
            if depth is d or depth > maxDepth:
                for i in queue:
                    newNode = TreeNode(v)
                    if i.left:
                        newNode.left = i.left
                    i.left = newNode
                    newNode = TreeNode(v)
                    if i.right:
                        newNode.right = i.right
                    i.right = newNode
                break
            count = len(queue)
            for i in range(count):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root


root = Tree.CreateTree([4, 2, 6, 3, 1, 5])
#Tree.BFSWalk(root, lambda node: print(node.val))

s = Solution()
v = 1
d = 1
s.addOneRow(root, v, d)
Tree.BFSWalk(root, lambda node: print(node.val))
