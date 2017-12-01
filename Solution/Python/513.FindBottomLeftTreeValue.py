class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        left = 0
        if(not root):
            return left
        result = []
        queue = [root]
        while(queue):
            count = len(queue)
            for i in range(0, count):
                node = queue.pop(0)
                if i == 0:
                    left = node.val
                if(node.left):
                    queue.append(node.left)
                if(node.right):
                    queue.append(node.right)
        return left
