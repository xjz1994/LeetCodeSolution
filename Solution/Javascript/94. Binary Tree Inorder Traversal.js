let Tree = require("../../Helper/Javascript/Tree").Tree;

let inorderTraversal = (root) => {
    let res = [];
    if (root == null) return res;
    let stack = [];
    var node = root;
    while (node != null || stack.length != 0) {
        while (node != null) {
            stack.push(node);
            node = node.left;
        }
        if (stack.length != 0) {
            node = stack.pop();
            res.push(node.val)
            node = node.right;
        }
    }
    return res;
}

let arr = [1, null, 2, 3];
let root = Tree.CreateTree(arr);
let res = inorderTraversal(root);
console.log(res);