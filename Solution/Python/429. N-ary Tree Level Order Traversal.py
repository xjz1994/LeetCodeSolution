# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res
        queue = [root]
        while queue:
            count = len(queue)
            level = []
            for i in range(count):
                node = queue.pop(0)
                level.append(node.val)
                queue += node.children
            res.append(level)
        return res
