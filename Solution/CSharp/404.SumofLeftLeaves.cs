public class Solution {
    private int sum = 0;
    public int SumOfLeftLeaves(TreeNode root) {
        if (root != null) {
            if (root.left != null && (root.left.left == null && root.left.right == null)) {
                sum += root.left.val;
            }
            SumOfLeftLeaves(root.left);
            SumOfLeftLeaves(root.right);
        }
        return sum;
    }
}