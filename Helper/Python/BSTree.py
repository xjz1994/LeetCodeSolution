# coding:utf-8
from Tree import *


class BSTree:
    # 创建二叉搜索树
    @staticmethod
    def CreateBSTree(rootVal, arr):
        """
        :type arr: int
        :type arr: list
        :rtype: TreeNode
        """
        root = Tree.CreateNode(rootVal)
        for i in range(0, len(arr)):
            if(arr[i]):
                BSTree.Insert(root, arr[i])
        return root

    @staticmethod
    def Insert(root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: void
        """
        node = root
        newNode = Tree.CreateNode(val)
        parent = None
        while node:
            parent = node
            if val > parent.val:
                node = node.right
            else:
                node = node.left
        if(not parent):
            return newNode
        elif val > parent.val:
            parent.right = newNode
        else:
            parent.left = newNode
