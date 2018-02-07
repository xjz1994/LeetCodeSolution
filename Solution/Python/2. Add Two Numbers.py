# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        node1, node2 = l1, l2
        newList = newNode = ListNode(0)
        carry = 0
        while node1 or node2 or carry:
            v1, v2 = 0, 0
            if node1:
                v1, node1 = node1.val, node1.next
            if node2:
                v2, node2 = node2.val, node2.next

            val = (v1 + v2 + carry)
            carry = 1 if val >= 10 else 0
            newNode.next = ListNode(val % 10)
            newNode = newNode.next
        return newList.next


l1 = ListNode(1)
# l1.next = ListNode(4)
# l1.next.next = ListNode(3)

l2 = ListNode(9)
l2.next = ListNode(9)
# l2.next.next = ListNode(4)
# l2.next.next.next = ListNode(3)

s = Solution()
newList = s.addTwoNumbers(l1, l2)
while newList:
    print(newList.val)
    newList = newList.next
