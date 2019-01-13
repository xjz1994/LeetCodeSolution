/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
let Tree = require('../../Helper/Javascript/Tree').Tree;

/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isUnivalTree = function (root) {
    if (root == null) {
        return false;
    }
    let isUnival = true;
    let val = root.val;
    let walk = (node) => {
        if (node.val != val) {
            isUnival = false;
            return;
        }
        if (node.left) {
            walk(node.left);
        }
        if (node.right) {
            walk(node.right)
        }
    }
    walk(root);
    return isUnival;
};

// let root = Tree.CreateTree([1, 1, 1, 1, 1, null, 1]);
// let root = Tree.CreateTree([2, 2, 2, 5, 2]);
let root = Tree.CreateTree([9, 9, 6, 9, 9]);
console.log(isUnivalTree(root));