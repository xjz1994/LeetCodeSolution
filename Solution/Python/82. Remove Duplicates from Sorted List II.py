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
        d = dict()
        node = head
        while node:
            d[node.val] = d.get(node.val, 0) + 1
            node = node.next

        key = []
        node = head
        while node:
            if d[node.val] == 1:
                key.append(node.val)
            node = node.next

        if not key:
            return None

        node = head
        for i in range(len(key)):
            k = key[i]
            node.val = k
            if i == len(key) - 1:
                node.next = None
            else:
                node = node.next

        return head


s = Solution()

# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(3)
# head.next.next.next.next = ListNode(4)
# head.next.next.next.next.next = ListNode(4)
# head.next.next.next.next.next.next = ListNode(5)
# newhead = s.deleteDuplicates(head)

head = ListNode(2)
head.next = ListNode(1)
newhead = s.deleteDuplicates(head)

while newhead:
    print(newhead.val)
    newhead = newhead.next
