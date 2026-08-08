class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def bfs(row, col):
            q = deque([(row, col)])
            while q:
                r, c = q.popleft()
                if (r < 0 or r == ROWS or
                    c < 0 or c == COLS or
                    grid[r][c] == '0'
                ):
                    continue
                grid[r][c] = '0'
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    q.append((nr, nc))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    bfs(r, c)
                    res += 1
        
        return res
