using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Algorithm {
	public class TreeNode {
		public int val;
		public TreeNode left;
		public TreeNode right;
		public TreeNode(int x) { val = x; }
	}

	public class Tree {

		public static TreeNode CreateNode(int? val) {
			if (val == null) return null;
			return new TreeNode((int) val);
		}

		public static TreeNode CreateTree(int?[] arr) {
			if (arr.Length <= 0 || arr[0] == null) {
				return null;
			}
			TreeNode root = Tree.CreateNode(arr[0]);
			var queue = new Queue<TreeNode>();
			queue.Enqueue(root);
			int index = 1;
			while (queue.Count > 0) {
				TreeNode node = queue.Dequeue();
				if (node == null) continue;
				if (index < arr.Length) {
					node.left = Tree.CreateNode(arr[index++]);
					queue.Enqueue(node.left);
				}
				if (index < arr.Length) {
					node.right = Tree.CreateNode(arr[index++]);
					queue.Enqueue(node.right);
				}
			}
			return root;
		}

		public static void Walk(TreeNode node, Action<TreeNode> func, TreeWalkType type) {
			if (node != null) {
				if (type == TreeWalkType.Pre) func(node);
				Walk(node.left, func, type);
				if (type == TreeWalkType.In) func(node);
				Walk(node.right, func, type);
				if (type == TreeWalkType.Post) func(node);
			}
		}

		//广度优先遍历
		public static void BFSWalk(TreeNode root, Action<TreeNode> func) {
			if (root == null) return;
			var queue = new Queue<TreeNode>();
			queue.Enqueue(root);
			while (queue.Count > 0) {
				TreeNode node = queue.Dequeue();
				func(node);
				if (node.left != null) queue.Enqueue(node.left);
				if (node.right != null) queue.Enqueue(node.right);
			}
		}

		//广度优先,逐层遍历
		public static void BFSWalkLevel(TreeNode root, Action<TreeNode> func) {
			if (root == null) return;
			var queue = new Queue<TreeNode>();
			queue.Enqueue(root);
			while (queue.Count > 0) {
				int count = queue.Count;
				for (int i = 0; i < count; i++) {
					TreeNode node = queue.Dequeue();
					func(node);
					if (node.left != null) queue.Enqueue(node.left);
					if (node.right != null) queue.Enqueue(node.right);
				}
			}
		}

		//深度优先，先序
		public static void DFSWalk(TreeNode root, Action<TreeNode> func) {
			if (root == null) return;
			var stack = new Stack<TreeNode>();
			stack.Push(root);
			while (stack.Count > 0) {
				var node = stack.Pop();
				func(node);
				if (node.right != null) stack.Push(node.right);
				if (node.left != null) stack.Push(node.left);
			}
		}

		//深度优先，中序
		public static void InOrderTreeWalk(TreeNode root, Action<TreeNode> func) {
			if (root == null) {
				return;
			}
			var stack = new Stack<TreeNode>();
			TreeNode current = root;
			while (current != null) {
				stack.Push(current);
				current = current.left;
			}
			while (stack.Count != 0) {
				current = stack.Pop();
				func(current); //func
				TreeNode node = current.right;
				while (node != null) {
					stack.Push(node);
					node = node.left;
				}
			}
		}
	}

	public enum TreeWalkType {
		Pre,
		In,
		Post
	}
}