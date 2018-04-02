class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 == None and t2 == None:
            return None
        elif t1 == None and t2 != None:
            return t2
        elif t1 != None and t2 == None:
            return t1
        self.Merge(t1, t2)
        return t1

    def Merge(self, t1, t2):
        if t1 != None and t2 != None:
            t1.val = t1.val + t2.val
            if t1.left != None and t2.left != None:
                self.Merge(t1.left, t2.left)
            if t1.right != None and t2.right != None:
                self.Merge(t1.right, t2.right)
        if t1.left == None and t2.left != None:
            t1.left = t2.left
        if t1.right == None and t2.right != None:
            t1.right = t2.right
