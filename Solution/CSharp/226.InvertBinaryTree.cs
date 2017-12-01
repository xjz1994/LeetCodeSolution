/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int x) { val = x; }
 */
public class Solution {
    public TreeNode InvertTree(TreeNode root) {
        if(root==null||(root.left==null&&root.right==null)) return root;
        var tem = root.left;
        root.left = root.right;
        root.right = tem;
        if(root.right!=null){
            InvertTree(root.right);
        }
        if(root.left!=null){
            InvertTree(root.left);
        }
        return root;
    }
}
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
