class ListNode {
    constructor(val) {
        this.val = val;
        this.next = null;
    }
}


module.exports.LinkList = class LinkList {
    static CreateNode(val) {
        return new ListNode(val)
    }

    static CreateLinkList(values) {
        let root;
        let curNode;
        for (let i in values) {
            let node = this.CreateNode(values[i]);
            if (!root) {
                root = node;
                continue;
            }
            let last = curNode || root;
            last.next = node;
            curNode = node;
        }
        return root;
    }

    static Walk(root) {
        let node = root;
        while (node) {
            console.log(node.val);
            node = node.next;
        }
    }
}