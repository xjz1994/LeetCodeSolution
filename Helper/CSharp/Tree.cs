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
			if (arr.Length <= 0 || arr[0] == null) return null;
			TreeNode root = Tree.CreateNode(arr[0]);
			Queue<TreeNode> queue = new Queue<TreeNode>();
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

		//递归先序遍历
		public static void RecursionWalk(TreeNode node, Action<TreeNode> func) {
			if (node == null) return;
			func(node);
			RecursionWalk(node.left, func);
			RecursionWalk(node.right, func);
		}

		//非递归，先序
		public static void PreOrderWalk(TreeNode root, Action<TreeNode> func) {
			if (root == null) return;
			Stack<TreeNode> stack = new Stack<TreeNode>();
			var node = root;
			while (node != null || stack.Count() != 0) {
				while (node != null) {
					stack.Push(node);
					func(node);
					node = node.left;
				}
				if (stack.Count() != 0) {
					node = stack.Pop();
					node = node.right;
				}
			}
		}

		//非递归，中序
		public static void InOrderWalk(TreeNode root, Action<TreeNode> func) {
			if (root == null) return;
			Stack<TreeNode> stack = new Stack<TreeNode>();
			var node = root;
			while (node != null || stack.Count() != 0) {
				while (node != null) {
					stack.Push(node);
					node = node.left;
				}
				if (stack.Count() != 0) {
					node = stack.Pop();
					func(node);
					node = node.right;
				}
			}
		}

		//非递归，后序
		public static void PostOrderWalk(TreeNode root, Action<TreeNode> func) {
			if (root == null) return;
			Stack<TreeNode> stack = new Stack<TreeNode>();
			var node = root;
			var lastVist = root;
			while (node != null || stack.Count() != 0) {
				while (node != null) {
					stack.Push(node);
					node = node.left;
				}
				node = stack.Peek();
				if (node.right == null || node.right == lastVist) {
					func(node);
					lastVist = node;
					node = null;
					stack.Pop();
				} else {
					node = node.right;
				}
			}
		}

		//广度优先遍历
		public static void BFSWalk(TreeNode root, Action<TreeNode> func) {
			if (root == null) return;
			Queue<TreeNode> queue = new Queue<TreeNode>();
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
			Queue<TreeNode> queue = new Queue<TreeNode>();
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
	}
}