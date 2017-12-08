/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public void Delete(ListNode node) {
        node.val = node.next.val;
        node.next = node.next.next;
    }

    public ListNode RemoveElements(ListNode head, int val) {
        ListNode node = head;
        ListNode last = null;
        while (node != null) {
            if (node.val == val) {
                if (node.next != null) {
                    Delete(node);
                    continue;
                } else {
                    if (last != null) {
                        last.next = null;
                    } else {
                        return null;
                    }
                }
            }
            last = node;
            node = node.next;
        }
        return head;
    }
}