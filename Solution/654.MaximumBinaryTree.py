



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None

        def helper(node, nums):
            index = nums.index(max(nums))
            leftArr = nums[:index]
            rightArr = nums[index + 1:]
            if leftArr:
                helper(node.left, leftArr)
            if rightArr:
                helper(node.right, rightArr)

        root = TreeNode(max(nums))
        helper(root, nums)
        return root
