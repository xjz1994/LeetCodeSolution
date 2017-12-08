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
        if (root == null || (root.left == null && root.right == null)) return root;
        var tem = root.left;
        root.left = root.right;
        root.right = tem;
        if (root.right != null) {
            InvertTree(root.right);
        }
        if (root.left != null) {
            InvertTree(root.left);
        }
        return root;
    }
}