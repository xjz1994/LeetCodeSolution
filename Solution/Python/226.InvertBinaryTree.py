class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if (not root):
            return
        queue = [root]
        while (queue):
            node = queue.pop(0)
            node.left,node.right = node.right,node.left
            if(node.left):
                queue.append(node.left)
            if(node.right):
                queue.append(node.right)
        return root