public class Solution {
    public ListNode ReverseList(ListNode head) {
        if (head == null) {
            return null;
        }
        Stack<int> stack = new Stack<int>();
        stack.Push(head.val);
        var node = head.next;
        while (node != null) {
            stack.Push(node.val);
            node = node.next;
        }

        head.val = stack.Pop();
        node = head.next;
        while (node != null) {
            node = node.next;
        }
        return head;
    }
}
public class Solution {
    public ListNode ReverseList(ListNode head) {
        if (head == null || head.next == null)
            return head;
        ListNode nextNode = head.next;
        ListNode newHead = ReverseList(nextNode);
        nextNode.next = head;
        head.next = null;
        return newHead;
    }
}