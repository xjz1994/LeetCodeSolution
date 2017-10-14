# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if(not root):
            return 0
        queue = [root]
        level = 1
        while(queue):
            count = len(queue)
            for i in range(0, count):
                node = queue.pop(0)
                if(not node.left and not node.right):
                    return level
                if(node.left):
                    queue.append(node.left)
                if(node.right):
                    queue.append(node.right)
            level += 1
