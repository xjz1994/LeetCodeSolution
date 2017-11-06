let Tree = require('../Helper/Javascript/Tree').Tree;

/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/**
 * @param {TreeNode} root
 * @return {string[][]}
 */
var printTree = function (root) {
    let rowNum = maxDepth(root);
    let colNum = Math.pow(2, rowNum - 1) * 2 - 1;
    let res = [];
    for (let i = 0; i < rowNum; i++) {
        res[i] = [];
        for (let j = 0; j < colNum; j++) {
            res[i][j] = "";
        }
    }
    setNodeNum(root, res, 0, 0, colNum);
    return res;
};

var setNodeNum = function (node, res, depth, left, right) {
    if (!node) return;
    let mid = Math.floor((left + right) / 2);
    res[depth][mid] = String(node.val);
    setNodeNum(node.left, res, depth + 1, left, mid);
    setNodeNum(node.right, res, depth + 1, mid, right);
}

var maxDepth = function (root) {
    if (!root) return 0;
    let left = maxDepth(root.left);
    let right = maxDepth(root.right);
    return Math.max(left, right) + 1;
}

let root = Tree.CreateTree([1, 2, 5, 3, null, null, null, 4, 5]);
console.log(printTree(root));