let Tree = require('../../Helper/Javascript/Tree').Tree;

/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/**
 * @param {TreeNode} root
 * @param {number} x
 * @param {number} y
 * @return {boolean}
 */
var isCousins = function (root, x, y) {
    if (root == null) {
        return false;
    }
    let queue = [root];
    while (queue.length > 0) {
        let size = queue.length;
        let isExitX = false;
        let isExitY = false;
        for (let i = 0; i < size; i++) {
            let node = queue.shift()
            if (node.val == x) { isExitX = true; }
            if (node.val == y) { isExitY = true; }
            if (node.left != null && node.right != null) {
                if (node.left.val == x && node.right.val == y) {
                    return false;
                }
                if (node.left.val == y && node.right.val == x) {
                    return false;
                }
            }
            if (node.left) { queue.push(node.left); }
            if (node.right) { queue.push(node.right); }
        }
        if (isExitX && isExitY) return true;
    }
    return false;
};

let root = [1, 2, 3, 4];
let x = 4;
let y = 3;
let treeRoot = Tree.CreateTree(root);
let res = isCousins(treeRoot, x, y);
console.log(res);