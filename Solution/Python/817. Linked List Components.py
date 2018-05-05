# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        res = 0
        gSet = set(G)
        while head:
            if head.val in gSet and(head.next == None or head.next.val not in gSet):
                res += 1
            head = head.next
        return res


head = ListNode(0)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
G = [0, 3, 1, 4]
s = Solution()
res = s.numComponents(head, G)
print(res)
