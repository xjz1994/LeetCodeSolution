# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None and headB == None:
            return None
        pa = headA
        pb = headB
        while pa != pb:
            pa = headB if pa == None else pa.next
            pb = headA if pb == None else pb.next
        return None


class Solution2(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        countA = countB = 0

        nodeA = headA
        nodeB = headB
        while nodeA or nodeB:
            if nodeA:
                countA += 1
                nodeA = nodeA.next
            if nodeB:
                countB += 1
                nodeB = nodeB.next

        nodeA = headA
        nodeB = headB
        while countA != countB:
            if countA > countB:
                nodeA = nodeA.next
                countA -= 1
            elif countA < countB:
                countB -= 1
                nodeB = nodeB.next

        while nodeA and nodeA != nodeB:
            nodeA = nodeA.next
            nodeB = nodeB.next

        return nodeA


c = ListNode(10)
c.next = ListNode(11)
c.next.next = ListNode(12)

a = ListNode(1)
a.next = ListNode(2)
a.next.next = c

b = ListNode(1)
b.next = ListNode(2)
b.next.next = ListNode(3)
b.next.next.next = c

res = Solution2().getIntersectionNode(a, b)
print(res.val)
