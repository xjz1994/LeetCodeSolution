using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Algorithm {
	class TreeNode {
	     public int val;
	     public TreeNode left;
	     public TreeNode right;
	     public TreeNode(int x) { val = x; }
	 }
	class Tree {
		public static TreeNode CreateNode(int? val) {
			if (val == null) return null;
			return new TreeNode((int)val);
		}
		public static TreeNode CreateTree(int?[] arr) {
			if (arr.Length <= 0 || arr[0] == null) {
				return null;
			}
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
		public static void Walk(TreeNode node, Action<TreeNode> func, TreeWalkType type) {
			if (node != null) {
				if (type == TreeWalkType.Pre) func(node);
				Walk(node.left, func, type);
				if (type == TreeWalkType.In) func(node);
				Walk(node.right, func, type);
				if (type == TreeWalkType.Post) func(node);
			}
		}
		//非递归，广度优先遍历
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
		//非递归，中序遍历
		public static void InOrderTreeWalk(TreeNode root, Action<TreeNode> func) {
			if (root == null) {
				return;
			}
			Stack<TreeNode> stack = new Stack<TreeNode>();
			TreeNode current = root;
			while (current != null) {
				stack.Push(current);
				current = current.left;
			}
			while (stack.Count != 0) {
				current = stack.Pop();
				func(current);             //func
				TreeNode node = current.right;
				while (node != null) {
					stack.Push(node);
					node = node.left;
				}
			}
		}
	}
	enum TreeWalkType {
		Pre,
		In,
		Post
	}
}