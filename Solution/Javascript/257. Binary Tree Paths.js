/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {string[]}
 */
var binaryTreePaths = function (root) {
    let res = [];

    let dfs = (node, res, string) => {
        if (node !== null) {
            string += node.val;
        }
        if (!node || (!node.left && !node.right)) {
            if (string.length > 0) {
                res.push(string);
            }
            return;
        }
        string = string + "->";
        if (node.left) {
            dfs(node.left, res, string);
        }
        if (node.right) {
            dfs(node.right, res, string);
        }
    }

    dfs(root, res, "");

    return res;
};