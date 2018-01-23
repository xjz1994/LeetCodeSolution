import random

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        # O(1) space
        self.head = head
        self.length = 0

        node = head
        while node:
            self.length += 1
            node = node.next

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        idx = random.randint(0, self.length - 1)
        node = self.head
        while idx:
            idx -= 1
            node = node.next
        return node.val



# Your Solution object will be instantiated and called as such:
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

obj = Solution(head)
param_1 = obj.getRandom()
print(param_1)
