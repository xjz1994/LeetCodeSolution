class Solution:
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        res, last = [], len(graph) - 1

        def search(node, path):
            if path[-1] == last:
                res.append(path[:])
                return
            for i in graph[node]:
                search(i, path + [i])

        search(0, [0])
        return res


s = Solution()
graph = [[1, 2], [3], [3], []]
res = s.allPathsSourceTarget(graph)
print(res)
