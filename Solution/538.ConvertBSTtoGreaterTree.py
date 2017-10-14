# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.helper(root)
        return root
        
        
    sum = 0
    def helper(self, node):
        if(node):
            self.helper(node.right)
            self.sum = node.val
            self.helper(node.left)
