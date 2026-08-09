class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(r, c):
            if (r < 0 or r == ROWS or
                c < 0 or c == COLS or
                grid[r][c] == 0
            ):
                return 0
            grid[r][c] = 0
            curLength = 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                curLength += dfs(nr, nc)
            return curLength

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    res = max(res, dfs(r, c))
        
        return res