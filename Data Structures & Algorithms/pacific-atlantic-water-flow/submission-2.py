class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        atl, pac = set(), set()
        res = []

        def dfs(r, c, visit, prev):
            if (min(r, c) < 0 or r >= ROWS or c >= COLS or
            heights[r][c] < prev or (r, c) in visit):
                return
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])
        
        for r in range(ROWS):
            dfs(r, 0, pac, 0)
            dfs(r, COLS - 1, atl, 0)
        for c in range(COLS):
            dfs(0, c, pac, 0)
            dfs(ROWS - 1, c, atl, 0)

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in atl and (r, c) in pac:
                    res.append([r, c])
        return res