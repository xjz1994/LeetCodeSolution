class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if not root:
            return result
        queue = [root]
        while queue:
            count = len(queue)
            res = -2147483648
            for i in range(count):
                curNode = queue.pop(0)
                res = max(curNode.val, res)
                if curNode.left:
                    queue.append(curNode.left)
                if curNode.right:
                    queue.append(curNode.right)
            result.append(res)
        return result
