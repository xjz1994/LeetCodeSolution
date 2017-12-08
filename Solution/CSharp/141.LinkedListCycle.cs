public class Solution {
    public bool HasCycle(ListNode head) {
        if (head == null) {
            return false;
        }
        ListNode node = head;
        HashSet<int> hashSet = new HashSet<int>();
        hashSet.Add(node.GetHashCode());
        while (node.next != null) {
            node = node.next;
            int hash = node.GetHashCode();
            if (hashSet.Contains(hash)) {
                return true;
            } else {
                hashSet.Add(hash);
            }
        }
        return false;
    }
}
public class Solution {
    public bool HasCycle(ListNode head) {
        if (head == null || head.next == null) {
            return false;
        }
        ListNode slow = head;
        ListNode fast = head;
        while (fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) {
                return true;
            }
        }
        return false;
    }
}