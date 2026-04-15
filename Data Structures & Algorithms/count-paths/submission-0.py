class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
    #    def dfs (i, j):
    #        # at bottom right
    #        if i == m - 1 and j == n - 1:
    #            return 1
    #        # check out of bounds
    #        if i == m or j == n:
    #            return 0
    #        
    #        return dfs(i, j+1) + dfs(i + 1, j)
#
#
#
    #    return dfs(0,0)

        row = [1] * n
        for i in range(m-2, -1, -1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j+1] + row[j]
            row = newRow

        return row[0]