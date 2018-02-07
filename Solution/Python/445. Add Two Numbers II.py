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
        def list2arr(root):
            res = []
            while root:
                res.append(root.val)
                root = root.next
            return res

        arr1, arr2 = list2arr(l1), list2arr(l2)
        index1, index2 = len(arr1) - 1, len(arr2) - 1
        carry = 0
        root = None
        while index1 >= 0 or index2 >= 0 or carry:
            v1, v2 = 0, 0
            if index1 >= 0:
                v1 = arr1[index1]
                index1 -= 1
            if index2 >= 0:
                v2 = arr2[index2]
                index2 -= 1

            val = (v1 + v2 + carry)
            carry = 1 if val >= 10 else 0

            newNode = ListNode(val % 10)
            newNode.next = root
            root = newNode

        return root


l1 = ListNode(7)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l1.next.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

s = Solution()
newList = s.addTwoNumbers(l1, l2)
while newList:
    print(newList.val)
    newList = newList.next
