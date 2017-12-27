class TreeNode {
    constructor(val) {
        this.val = val;
        this.left = this.right = null;
    }
}

module.exports.Tree = class Tree {
    static CreateNode(val) {
        if (val === null) {
            return null;
        }
        return new TreeNode(val);
    }

    static CreateTree(arr) {
        if (arr === null || arr.length == 0) {
            return null;
        }
        let root = Tree.CreateNode(arr[0]);
        let queue = [root];
        let index = 1;
        while (queue.length > 0) {
            let node = queue.shift();
            if (node === null) {
                continue;
            }
            if (index < arr.length) {
                node.left = Tree.CreateNode(arr[index])
                queue.push(node.left)
                index += 1
            }
            if (index < arr.length) {
                node.right = Tree.CreateNode(arr[index])
                queue.push(node.right)
                index += 1
            }
        }
        return root;
    }

    static Walk(node, fn) {
        if (node === null) return;
        fn(node);
        Tree.Walk(node.left, fn);
        Tree.Walk(node.right, fn);
    }

    static BFSWalk(node, fn) {
        if (node === null) return;
        let queue = [node];
        while (queue.length > 0) {
            let node = queue.shift();
            fn(node);
            if (node.left) {
                queue.push(node.left);
            }
            if (node.right) {
                queue.push(node.right);
            }
        }
    }

    //非递归中序遍历
    static InorderTraversal(root) {
        if (root == null) return;
        let stack = [];
        var node = root;
        while (node != null || stack.length != 0) {
            while (node != null) {
                stack.push(node);
                node = node.left;
            }
            if (stack.length != 0) {
                node = stack.pop();
                console.log(node.val)
                node = node.right;
            }
        }
        return res;
    }

}