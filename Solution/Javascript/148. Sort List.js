/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

let LinkList = require("../../Helper/Javascript/LinkList").LinkList;



function ListNode(val) {
    this.val = val;
    this.next = null;
}

var merge = function (head1, head2) {
    let d = new ListNode(0);
    let e = d;
    while (head1 || head2) {
        if (head1 && (!head2 || head1.val <= head2.val)) {
            e = e.next = head1;
            head1 = head1.next;
        }
        if (head2 && (!head1 || head2.val < head1.val)) {
            e = e.next = head2;
            head2 = head2.next;
        }
    }
    // 断开
    e.next = null;
    return d.next;
}

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var sortList = function (head) {
    if (!head || !head.next) {
        return head;
    }
    // 找到中间的node
    let slow = head;
    let fast = head.next;
    while (fast && fast.next) {
        fast = fast.next.next
        slow = slow.next
    }
    let mid = slow.next;
    // 断开
    slow.next = null;
    return merge(sortList(head), sortList(mid))
};

let arr = [4, 2, 1, 3];
let head = LinkList.CreateLinkList(arr);
let res = sortList(head);
LinkList.Walk(res);