/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int x) { val = x; }
 * }
 **/
public class Solution {
    public int tilt = 0;

    public int FindTilt(TreeNode root) {
        GetTilt(root);
        return tilt;
    }

    public int GetTilt(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int l = 0;
        int r = 0;
        if (root.left != null) {
            l = GetTilt(root.left);
        }
        if (root.right != null) {
            r = GetTilt(root.right);
        }
        tilt += Math.Abs(l - r);
        return l + r + root.val;
    }
}