less than or equal to
greater than or equal to

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
    public int[] FindMode(TreeNode root) {
        List<int> modes = new List<int>();
        int modeCount = 0, lastValue = int.MinValue, lastValueCount = 0;

        Stack<TreeNode> stack = new Stack<TreeNode>();
        TreeNode current = root;

        while (current != null) {
            stack.Push(current);
            current = current.left;
        }
        while (stack.Count != 0) {
            current = stack.Pop();

            if (current.val == lastValue) {
                lastValueCount++;
            } else {
                lastValue = current.val;
                lastValueCount = 1;
            }

            if (lastValueCount > modeCount) {
                modes.Clear();
                modes.Add(current.val);
                modeCount = lastValueCount;
            } else if (lastValueCount == modeCount) {
                modes.Add(current.val);
            }

            TreeNode node = current.right;
            while (node != null) {
                stack.Push(node);
                node = node.left;
            }
        }

        return modes.ToArray();
    }
}