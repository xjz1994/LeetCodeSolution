/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */


let Tree = require('../Helper/Javascript/Tree').Tree;

/**
 * @param {TreeNode} root
 * @return {string[][]}
 */
var printTree = function (root) {

};

let root = Tree.CreateTree([1, 2, 3, null, 4, null, null, null, null, 1, 2,]);
Tree.BFSRead(root);