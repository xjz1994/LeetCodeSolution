# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        node = head
        while node.next:
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next
        return head


s = Solution()

head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(3)

newHead = s.deleteDuplicates(head)

while newHead:
    print(newHead.val)
    newHead = newHead.next
