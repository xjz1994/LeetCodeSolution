class TreeNode {
    constructor(val) {
        this.val = val;
        this.left = this.right = null;
    }
}

module.exports.BSTree = class BSTree {
    static CreateNode(val) {
        if (val === null) {
            return null;
        }
        return new TreeNode(val);
    }

    static InsertNode(root, val) {
        let node = root;
        let newNode = BSTree.CreateNode(val);
        let parent = null;
        while (node !== null) {
            parent = node;
            if (val > parent.val) {
                node = node.right;
            } else {
                node = node.left;
            }
        }
        if (parent === null) {
            return newNode;
        } else if (val > parent.val) {
            parent.right = newNode;
        } else {
            parent.left = newNode;
        }
    }

    static CreateTree(rootVal, valArr) {
        let root = BSTree.CreateNode(rootVal);
        for (let i = 0; i < valArr.length; i++) {
            BSTree.InsertNode(root, valArr[i]);
        }
        return root
    }
}