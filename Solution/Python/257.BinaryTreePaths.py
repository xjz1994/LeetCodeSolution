# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        if not root:
            return []
        result = []
        self.dfs(root, result, "")
        return result

    def dfs(self, node, result, string):
        if not node.left and not node.right:
            result.append(string + str(node.val))
        if node.left:
            self.dfs(node.left, result, string + str(node.val) + "->")
        if node.right:
            self.dfs(node.right, result, string + str(node.val) + "->")
        
