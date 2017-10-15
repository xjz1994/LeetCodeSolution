
module.exports.TreeWalkType = TreeWalkType = {
    Pre: 0,
    In: 1,
    Post: 2
}

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

    static Walk(node, walkType, fn) {
        if (node === null) return;
        (walkType == TreeWalkType.Pre) && fn(node)
        Tree.Walk(node.left, walkType, fn);
        (walkType == TreeWalkType.In) && fn(node)
        Tree.Walk(node.right, walkType, fn);
        (walkType == TreeWalkType.Post) && fn(node)
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

    static BFSRead(node) {
        let isNull = (element, index, array) => {
            return (element === null);
        }
        if (node === null) return;
        let queue = [node];
        while (queue.length > 0 && !queue.every(isNull)) {
            let node = queue.shift();
            if (node) {
                console.log(node.val);
                queue.push(node.left);
                queue.push(node.right);
            } else {
                console.log("null");
            }
        }
    }
}