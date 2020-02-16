let LinkList = require("../../Helper/Javascript/LinkList").LinkList

/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {number}
 */
var getDecimalValue = function (head) {
    let res = 0;
    let node = head;
    while (node) {
        res = res * 2 + node.val
        node = node.next;
    }
    return res;
};

let head = [1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0]
head = LinkList.CreateLinkList(head)
let res = getDecimalValue(head)
console.log(res)