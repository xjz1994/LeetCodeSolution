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
            /**
             * =D3=C3#=B1=ED=CA=BE=BA=A2=D7=D3=BD=DA=B5=E3=CA=C7=B7=F1=CE=AAnull=B5=C4=C7=E9=BF=F6
             * =D3=C3","=BA=C5=B7=D6=B8=F4=BD=DA=B5=E3=CA=C7=B7=C0=D6=B9"12##"=BA=CD"2##"=D5=E2=D6=D6=C7=E9=BF=F6
             * ",12##",",2##"
             */
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