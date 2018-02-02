# coding:utf-8
from enum import Enum


class TreeWalkType(Enum):
    Pre = 0
    In = 1
    Post = 2


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Tree(object):
    # 创建节点
    @staticmethod
    def CreateNode(val):
        """
        :type val: int
        :rtype: TreeNode
        """
        if val:
            return TreeNode(val)
        return None

    # 创建二叉树
    @staticmethod
    def CreateTree(arr):
        """
        :type arr: list
        :rtype: TreeNode
        """
        if (len(arr) <= 0 or arr[0] is None):
            return None
        root = TreeNode(arr[0])
        queue = [root]
        index = 1
        while queue:
            node = queue.pop(0)
            if(node is None):
                continue
            if(index < len(arr)):
                node.left = Tree.CreateNode(arr[index])
                queue.append(node.left)
                index += 1
            if(index < len(arr)):
                node.right = Tree.CreateNode(arr[index])
                queue.append(node.right)
                index += 1
        return root

    # 遍历
    @staticmethod
    def Walk(node, walkType, func):
        """
        :type node: TreeNode
        :type walkType: TreeWalkType
        :type func: lambda
        :rtype: void
        """
        if(node):
            walkType is TreeWalkType.Pre and func(node)
            Tree.Walk(node.left, walkType, func)
            walkType is TreeWalkType.In and func(node)
            Tree.Walk(node.right, walkType, func)
            walkType is TreeWalkType.Post and func(node)

    # 广度优先遍历
    @staticmethod
    def BFSWalk(root, func):
        """
        :type root: TreeNode
        :type func: lambda
        :rtype: void
        """
        queue = [root]
        while queue:
            node = queue.pop(0)
            func(node)
            if(node.left):
                queue.append(node.left)
            if(node.right):
                queue.append(node.right)

    # 广度优先遍历每一层
    @staticmethod
    def WalkAllLevel(root, func):
        queue = [root]
        while queue:
            count = len(queue)
            for i in range(count):
                node = queue.pop(0)
                func(node)
                if(node.left):
                    queue.append(node.left)
                if(node.right):
                    queue.append(node.right)

    # 非递归，中序遍历
    @staticmethod
    def InOrderWalk(root, func):
        if(not root):
            return
        stack = []
        current = root
        while(current != None):
            stack.append(current)
            current = current.left
        while(stack):
            current = stack.pop()
            func(current)
            node = current.right
            while(node != None):
                stack.append(node)
                node = node.left

    # 使用迭代，对二叉树进行先序遍历
    @staticmethod
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = [root]
        while stack and stack[0]:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res

    @staticmethod
    def Tree2Array(root):
        res = []
        queue = [root]
        while queue and any(queue):
            node = queue.pop(0)
            if node:
                res.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append(None)
        return res
