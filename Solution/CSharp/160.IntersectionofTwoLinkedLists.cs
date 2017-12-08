/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode GetIntersectionNode(ListNode headA, ListNode headB) {
        int countA = GetCount(headA);
        int countB = GetCount(headB);
        int offset = Math.Abs(countA - countB);

        if (countA > countB) {
            headA = GetIndex(headA, offset);
            headB = GetIndex(headB, offset);
        }

        while (headA != null && headB != null) {
            if (headA.GetHashCode() == headB.GetHashCode()) {
                return headA;
            } else {
                headA = headA.next;
                headB = headB.next;
            }
        }
        return null;
    }

    public ListNode GetIndex(ListNode head, int index) {
        int count = 0;
        ListNode node = head;
        if (count == index) {
            return node;
        } else {
            count++;
            node = node.next;
        }
    }
    return null;
}

public int GetCount(ListNode head) {
    int count = 0;
    ListNode node = head;
    while (node != null) {
        count++;
        node = node.next;
    }
    return count;
}
}