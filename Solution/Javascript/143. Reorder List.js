let LinkList = require("../../Helper/Javascript/LinkList").LinkList;

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {void} Do not return anything, modify head in-place instead.
 */
var reorderList = function (head) {
    let arr = [];
    let node = head;
    while (node) {
        arr.push(node);
        node = node.next;
    }

    node = head;
    let left = 1;
    let right = arr.length - 1;
    while (left <= right) {
        node.next = arr[right];
        right--;
        node = node.next
        node.next = arr[left];
        left++;
        node = node.next;
    }

    if (node) {
        node.next = null;
    }
};

let list = LinkList.CreateLinkList([1, 2, 3, 4]);
reorderList(list);
LinkList.Walk(list);

