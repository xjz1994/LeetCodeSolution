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
    public bool IsSymmetric(TreeNode root) {
        if (root == null) return true;
        Queue<TreeNode> queue = new Queue<TreeNode>();
        queue.Enqueue(root);
        while (queue.Count > 0) {
            int count = queue.Count;
            List<int?> nextLevel = new List<int?>();
            for (int i = 0; i < count; i++) {
                TreeNode curNode = queue.Dequeue();
                if (curNode.left != null) {
                    queue.Enqueue(curNode.left);
                    nextLevel.Add(curNode.left.val);
                } else {
                    nextLevel.Add(null);
                }
                if (curNode.right != null) {
                    queue.Enqueue(curNode.right);
                    nextLevel.Add(curNode.right.val);
                } else {
                    nextLevel.Add(null);
                }
            }
            if (!LevelIsSymmetric(nextLevel)) {
                return false;
            }
        }
        return true;

        public bool LevelIsSymmetric(List<int?> list) {
            int left = 0;
            int right = list.Count - 1;
            while (right > left) {
                if (list[left++] != list[right--]) {
                    return false;
                }
            }
            return true;
        }
    }