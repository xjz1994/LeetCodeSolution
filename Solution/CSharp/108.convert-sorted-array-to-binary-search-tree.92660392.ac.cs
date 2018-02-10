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
    public TreeNode SortedArrayToBST(int[] nums) {
    	if (nums.Length == 0) {
    		return null;
    	}
    	return InsertNode(nums, 0, nums.Length - 1);
    }
    
    public TreeNode InsertNode(int[] nums,int l,int r) {
    	int m = (l + r) / 2;
    	TreeNode newNode = new TreeNode(nums[m]);
    	if (l < m) {
    		newNode.left = InsertNode(nums, l, m - 1);
    	}
    	if (r > m) {
    		newNode.right = InsertNode(nums, m + 1, r);
    	}
    	return newNode;
    }
}
