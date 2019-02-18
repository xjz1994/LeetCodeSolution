let Tree = require("../../Helper/Javascript/Tree").Tree;

/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} L
 * @param {number} R
 * @return {number}
 */
var rangeSumBST = function (root, L, R) {
    let sum = 0
    let stack = [root]
    while (stack.length > 0) {
        root = stack.pop()
        if (!root) continue;
        if (root.val < L) {
            stack.push(root.right)
        } else if (root.val > R) {
            stack.push(root.left)
        } else {
            sum += root.val
            stack.push(root.left)
            stack.push(root.right)
        }
    }
    return sum
};

// let arr = [10, 5, 15, 3, 7, null, 18];
// let root = Tree.CreateTree(arr);
// let L = 7;
// let R = 15;

let arr = [10, 5, 15, 3, 7, 13, 18, 1, null, 6];
let root = Tree.CreateTree(arr);
let L = 6;
let R = 10;

let res = rangeSumBST(root, L, R);
console.log(res);