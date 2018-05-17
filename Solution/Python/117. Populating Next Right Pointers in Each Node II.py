import sys
sys.path.append(
    r'F:\xjzspace\space\LeetCodeSolution\Helper\Python')
from Tree import *

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        queue = [root]
        while queue and queue[0]:
            count = len(queue)
            for i in range(count):
                node = queue.pop(0)
                if i < count - 1:
                    node.next = queue[0]
                else:
                    node.next = None
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)


root = Tree.CreateTree([1, 2, 3, 4, 5, None, 7])
Solution().connect(root)
print(root)
