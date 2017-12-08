/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public TreeNode MergeTrees(TreeNode t1, TreeNode t2) {
        if (t1 == null) return t1;
        if (t2 == null) return t2;
        Merge(t1, t2);
        return t1;
    }

    public void Merge(TreeNode t1, TreeNode t2) {
        if (t1 != null && t2 != null) {
            t1.val = t1.val + t2.val;
            if (t1.left != null && t2.left != null) {
                Merge(t1.left, t2.left);
            }
            if (t1.right != null && t2.right != null) {
                Merge(t1.right, t2.right);
            }
        }
        if (t1.left == null && t2.left != null) {
            t1.left = t2.left;
        }
        if (t1.right == null && t2.right != null) {
            t1.right = t2.right;
        }
    }
}