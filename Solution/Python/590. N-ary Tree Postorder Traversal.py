# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []

        def walk(node):
            if node:
                for child in node.children:
                    walk(child)
                res.append(node.val)
        walk(root)
        return res
