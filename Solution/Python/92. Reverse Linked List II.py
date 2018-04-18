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
        return head


s = Solution()

# 1->2->3->4->5->NULL
# 1->4->3->2->5->NULL
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

newHead = s.reverseBetween(head, 2, 4)
while newHead:
    print(newHead.val)
    newHead = newHead.next
