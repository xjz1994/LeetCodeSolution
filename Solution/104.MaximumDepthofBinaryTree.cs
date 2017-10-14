public int MaxDepth(TreeNode root) {
	if (root == null) {
		return 0;
	}
	int left = MaxDepth(root.left) + 1;
	int right = MaxDepth(root.right) + 1;
	return left > right ? left : right;
}
