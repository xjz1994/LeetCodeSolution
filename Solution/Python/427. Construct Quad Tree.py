# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        if not grid:
            return None

        def gen(row, col, l):
            if l == 1:
                node = Node(grid[row][col] == 1, True, None, None, None, None)
            else:
                halfL = l//2
                topLeft = gen(row, col, halfL)
                topRight = gen(row, col+halfL, halfL)
                bottomLeft = gen(row+halfL, col, halfL)
                bottomRight = gen(row+halfL, col+halfL, halfL)
                val = topLeft.val or topRight.val or bottomLeft.val or bottomRight.val
                isLeaf = topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf
                isSameVal = topLeft.val == topRight.val == bottomLeft.val == bottomRight.val
                if isLeaf and isSameVal:
                    node = Node(val, True, None, None, None, None)
                else:
                    node = Node(val, False, topLeft, topRight,
                                bottomLeft, bottomRight)
            return node

        return gen(0, 0, len(grid))


grid = [
    [1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0]
]

res = Solution().construct(grid)
print(res)
