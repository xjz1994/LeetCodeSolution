

class Solution(object):
    def imageSmoother(self, M):
        import math
        result = []
        for i in range(len(M)):
            row = []
            for j in range(len(M[i])):
                pos = [
                    [i - 1, j - 1], [i - 1, j], [i - 1, j + 1],
                    [i, j - 1], [i, j], [i, j + 1],
                    [i + 1, j - 1], [i + 1, j], [i + 1, j + 1]
                ]
                near = []
                for item in pos:
                    if item[0] >= 0 and item[0] < len(M) and item[1] >= 0 and item[1] < len(M[i]):
                        near.append(M[item[0]][item[1]])
                row.append(int(sum(near) / len(near)))
            result.append(row)
        return result
