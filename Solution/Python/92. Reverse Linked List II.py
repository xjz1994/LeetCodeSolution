class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        start = end = head
        for i in range(1, m):
            start = start.next
        for i in range(1, n):
            end = end.next

        stack = []
        s, e = start, end
        while s != e:
            stack.append(s.val)
            s = s.next
        stack.append(e.val)

        s, e = start, end
        while s != e:
            s.val = stack.pop()
            s = s.next
        e.val = stack.pop()

        return head


s = Solution()

# 1->2->3->4->5->NULL
# 1->4->3->2->5->NULL
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

#newHead = s.reverseBetween(head, 2, 2)
newHead = s.reverseBetween(head, 2, 3)
#newHead = s.reverseBetween(head, 2, 4)
while newHead:
    print(newHead.val)
    newHead = newHead.next
