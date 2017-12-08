using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Algorithm;

namespace Solution {

	public class Solution1 {
		public int MaxDepth(TreeNode root) {
			if (root == null) return 0;
			int left = MaxDepth(root.left) + 1;
			int right = MaxDepth(root.right) + 1;
			return left > right ? left : right;
		}
	}

	public class Solution2 {
		public int MaxDepth(TreeNode root) {
			if (root == null) return 0;
			return Math.Max(MaxDepth(root.left), MaxDepth(root.right)) + 1;
		}
	}

	public class Solution3 {
		public int MaxDepth(TreeNode root) {
			if (root == null) return 0;
			int depth = 0;
			Queue<TreeNode> queue = new Queue<TreeNode>();
			queue.Enqueue(root);
			while (queue.Count > 0) {
				int count = queue.Count;
				for (int i = 0; i < count; i++) {
					TreeNode node = queue.Dequeue();
					if (node.left != null) queue.Enqueue(node.left);
					if (node.right != null) queue.Enqueue(node.right);
				}
				depth++;
			}
			return depth;
		}
	}

	class Program {
		static void Main(string[] args) {
			Solution s = new Solution2();
			int?[] arr = { 1, 2, 3, 4, 5, null, 6, 7, 8, null, null, 9, 10 };
			TreeNode root = Tree.CreateTree(arr);
			int res = s.MaxDepth(root);
			Console.Write(res);
		}
	}
}