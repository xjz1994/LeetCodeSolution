2202
3988
Easy
love_Fawn
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public string Tree2str(TreeNode t) {
        if (t == null) return "";
        return DFS(t);
    }

    static public string DFS(TreeNode t) {
        StringBuilder builder = new StringBuilder();
        builder.Append(t.val);
        if (t.left != null) {
            builder.Append("(");
            builder.Append(DFS(t.left));
            builder.Append(")");
        }
        if (t.right != null) {
            if (t.left == null) {
                builder.Append("()");
            }
            builder.Append("(");
            builder.Append(DFS(t.right));
            builder.Append(")");
        }
        return builder.ToString();
    }
}