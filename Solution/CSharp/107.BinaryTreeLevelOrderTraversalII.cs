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
    public List<List<int>> LevelOrderBottom(TreeNode root) {
        List<List<int>> result = new List<List<int>>();
        if (root == null) return result;
        Queue<TreeNode> queue = new Queue<TreeNode>();
        queue.Enqueue(root);
        while (queue.Count > 0) {
            List<int> curLevel = new List<int>();
            int count = queue.Count;
            for (int i = 0; i < count; i++) {
                TreeNode curNode = queue.Dequeue();
                curLevel.Add(curNode.val);
                if (curNode.left != null) queue.Enqueue(curNode.left);
                if (curNode.right != null) queue.Enqueue(curNode.right);
            }
        }
        result.Reverse();
        return result;
    }
}