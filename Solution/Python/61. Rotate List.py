# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        tail = head
        nodeSum = 1

        while tail.next:
            tail = tail.next
            nodeSum += 1

        tail.next = head

        k = k % nodeSum
        for i in range(nodeSum - k):
            tail = tail.next

        head = tail.next
        tail.next = None
        return head


s = Solution()

# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)
# res = s.rotateRight(head, 2)

head = ListNode(0)
res = s.rotateRight(head, 1)

# head = ListNode(1)
# res = s.rotateRight(head, 99)

# head = ListNode(1)
# head.next = ListNode(2)
# res = s.rotateRight(head, 1)

while res:
    print(res.val)
    res = res.next
