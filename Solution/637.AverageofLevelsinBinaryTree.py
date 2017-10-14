# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        """        
        if(not root):
            return 0
        result = []
        queue = [root]
        while(queue):
            count = len(queue)
            sum = 0
            for i in range(0, count):
                node = queue.pop(0)
                sum += node.val
                if(node.left):
                    queue.append(node.left)
                if(node.right):
                    queue.append(node.right)
            result.append(sum * 1.0 / count)
        return result
