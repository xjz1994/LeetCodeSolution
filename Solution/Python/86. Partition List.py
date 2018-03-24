# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        left = []
        right = []
        node = head
        while node:
            if node.val < x:
                left.append(node.val)
            else:
                right.append(node.val)
            node = node.next

        lIdx = 0
        rIdx = 0
        node = head
        while node:
            if lIdx < len(left):
                node.val = left[lIdx]
                lIdx += 1
            elif rIdx < len(right):
                node.val = right[rIdx]
                rIdx += 1
            node = node.next

        return head


s = Solution()

head = ListNode(1)
head.next = ListNode(4)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(2)
newhead = s.partition(head, 4)

while newhead:
    print(newhead.val)
    newhead = newhead.next
