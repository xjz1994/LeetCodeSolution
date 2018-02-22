# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        slow = fast = head
        for i in range(n):
            fast = fast.next

        if not fast:
            return head.next  # 移除第一个节点的情况

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return head


s = Solution()

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
newhead = s.removeNthFromEnd(head, 5)

while newhead:
    print(newhead.val)
    newhead = newhead.next
