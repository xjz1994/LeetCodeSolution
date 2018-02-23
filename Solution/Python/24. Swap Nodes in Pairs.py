# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        left = head
        right = head.next

        if not right:
            return head

        right = left.next
        left.next = right.next
        right.next = left

        head = right
        right = right.next

        while right.next and right.next.next:
            temL, temR = right.next, right.next.next
            right.next = temR
            temN = temR.next
            temR.next = temL
            temL.next = temN

            right = right.next.next

        return head


class Solution2:
    def swapPairs(self, head):
        if not head:
            return None
        p1, p2 = head, head.next
        while p2:
            p1.val, p2.val = p2.val, p1.val
            p1 = p2.next
            p2 = p1.next if p1 else p1
        return head


s = Solution2()

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
newhead = s.swapPairs(head)

while newhead:
    print(newhead.val)
    newhead = newhead.next
