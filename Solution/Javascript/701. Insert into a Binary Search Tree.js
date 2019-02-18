let Tree = require("../../Helper/Javascript/Tree").Tree;

/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

function TreeNode(val) {
    this.val = val;
    this.left = this.right = null;
}

var insertNode = function (root, val) {
    let node = root;
    let newNode = new TreeNode(val);
    let parent = null;
    while (node != null) {
        parent = node;
        if (val > parent.val) {
            node = node.right;
        } else {
            node = node.left;
        }
    }
    if (parent == null) {
        return newNode;
    } else if (val > parent.val) {
        parent.right = newNode;
    } else {
        parent.left = newNode;
    }
}

/**
 * @param {TreeNode} root
 * @param {number} val
 * @return {TreeNode}
 */
// var insertIntoBST = function (root, val) {
//     let newRoot = new TreeNode(val);
//     let stack = [root];
//     while (stack.length > 0) {
//         let node = stack.pop();
//         if (node == null) {
//             continue;
//         }
//         if (node.left) {
//             stack.push(node.left);
//         }
//         if (node.right) {
//             stack.push(node.right);
//         }
//         insertNode(newRoot, node.val);
//     }
//     return newRoot;
// };


var insertIntoBST = function (root, val) {
    if (root == null) {
        return new TreeNode(val);
    }
    if (root.val > val) {
        root.left = insertIntoBST(root.left, val);
    } else {
        root.right = insertIntoBST(root.right, val);
    }
    return root;
};

let arr = [4, 2, 7, 1, 3];
let root = Tree.CreateTree(arr);
let val = 5;
let res = insertIntoBST(root, val);
console.log(res)