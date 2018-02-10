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
    public bool IsSubtree(TreeNode s, TreeNode t) {
        string s1 = Tree2String(s);
        string s2 = Tree2String(t);

        return s1.Contains(s2) || s2.Contains(s1);
    }

    static public string Tree2String(TreeNode root) {
        if (root == null) {
            return "";
        }
        StringBuilder sb = new StringBuilder();

        Stack<TreeNode> stack = new Stack<TreeNode>();
        TreeNode current = root;

        stack.Push(current);

        while (stack.Count != 0) {
            TreeNode popelem = stack.Pop();

            if (popelem == null) {
                sb.Append("#");
            } else { }
            if (popelem != null) {
                stack.Push(popelem.right);
                stack.Push(popelem.left);
            }
        }

        return sb.ToString();
    }
}