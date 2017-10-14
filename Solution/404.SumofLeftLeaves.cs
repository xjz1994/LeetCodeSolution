public class Solution {
    private int sum = 0;
    public int SumOfLeftLeaves(TreeNode root) {
		if (root != null) {
			if(root.left != null &amp;&amp; (root.left.left == null &amp;&amp; root.left.right == null)){
			    sum += root.left.val;
			}
			SumOfLeftLeaves(root.left);
			SumOfLeftLeaves(root.right);
		}
		return sum;
    }
}
