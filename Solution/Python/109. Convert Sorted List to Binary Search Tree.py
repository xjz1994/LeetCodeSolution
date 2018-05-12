import sys
sys.path.append(
    r'F:\xjzspace\space\LeetCodeSolution\Helper\Python')
from Tree import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head :
            return None
        if not head.next :
            return TreeNode(head.val)
        
        slow , fast = head ,head.next.next
        
        while fast and fast.next :
            fast = fast.next.next
            slow = slow.next
        
        curr = slow.next
        slow.next = None
        
        root = TreeNode(curr.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(curr.next)
        
        return root

    # def sortedListToBST(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: TreeNode
    #     """
    #     nums = []
    #     while head:
    #         nums.append(head.val)
    #         head = head.next

    #     if not nums:
    #         return None

    #     def insert(nums, l, r):
    #         m = (l+r) // 2
    #         newNode = TreeNode(nums[m])
    #         if l < m:
    #             newNode.left = insert(nums, l, m-1)
    #         if r > m:
    #             newNode.right = insert(nums, m+1, r)
    #         return newNode

    #     return insert(nums, 0, len(nums)-1)


head = ListNode(10)
head.next = ListNode(-3)
head.next.next = ListNode(0)
head.next.next.next = ListNode(5)
head.next.next.next.next = ListNode(9)

root = Solution().sortedListToBST(head)
res = Tree.Tree2Array(root)
print(res)