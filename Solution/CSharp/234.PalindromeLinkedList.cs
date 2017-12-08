/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 * }
 */
public class Solution {
    public ListNode ReverseList(ListNode head) {
        if (head == null || head.next == null)
            ListNode nextNode = head.next;
        ListNode newHead = ReverseList(nextNode);
        nextNode.next = head;
        head.next = null;
        return newHead;
    }

    public ListNode FindMid(ListNode head) {
        ListNode fast = head;
        ListNode slow = head;
        int num = 1;
        while (fast != null) {
            num++;
            if (fast.next != null) {
                fast = fast.next.next;
            } else {
                break;
            }
            slow = slow.next;
        }
        return slow;
    }

    public bool IsPalindrome(ListNode head) {
        if (head == null) {
            return true;
        }
        ListNode midNode = FindMid(head);
        ListNode newMid = ReverseList(midNode);
        ListNode font = head;
        ListNode back = newMid;
        while (back != null) {
            if (font.val != back.val) {
                return false;
            }
            font = font.next;
            back = back.next;
        }
        return true;
    }
}