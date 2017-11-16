let LinkList = require('../Helper/Javascript/LinkList').LinkList;


var splitListToParts = function (root, k) {
    let nodeArr = [];
    let node = root;
    while (node) {
        nodeArr.push(node.val);
        node = node.next;
    }
    let res = [];
    let startIndex = 0;
    let mod = nodeArr.length % k;
    let quo = Math.floor(nodeArr.length / k);
    for (let i = 0; i < k; i++) {
        let length = mod-- > 0 ? quo + 1 : quo;
        res.push(nodeArr.slice(startIndex, startIndex + length));
        startIndex += length;
    }
    return res;
};

// let root = LinkList.CreateLinkList([]);
// let res = splitListToParts(root, 3)
// let root = LinkList.CreateLinkList([1, 2, 3]);
// let res = splitListToParts(root, 5)

