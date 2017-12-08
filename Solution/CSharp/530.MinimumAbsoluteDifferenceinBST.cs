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
    public int GetMinimumDifference(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int min = Int32.MaxValue;
        Stack<TreeNode> stack = new Stack<TreeNode>();
        TreeNode current = root;

        while (current != null) {
            stack.Push(current);
            current = current.left;
        }
        while (stack.Count != 0) {
            current = stack.Pop();

            if (stack.Count > 0) {
                int diff = Math.Abs(stack.Peek().val - current.val);
                min = Math.Min(diff, min);
            }

            TreeNode node = current.right;
            while (node != null) {
                stack.Push(node);
                node = node.left;

                if (stack.Count > 0) {
                    int diff = Math.Abs(stack.Peek().val - current.val);
                    min = Math.Min(diff, min);
                }

            }
        }
        return min;
    }
}