public class Solution {
    public ListNode MergeTwoLists(ListNode l1, ListNode l2) {
        ListNode curNode = null;
        ListNode headNode = new ListNode(-1);
        curNode = headNode;
        while (l1 != null && l2 != null) {
            if (l1.val < l2.val) {
                curNode.next = l1;
                l1 = l1.next;
            } else {
                curNode.next = l2;
                l2 = l2.next;
            }
            curNode = curNode.next;
        }
        if (l2 != null) {
            curNode.next = l2;
        } else if (l1 != null)
            curNode.next = l1;
    }
    return headNode.next;
}
}