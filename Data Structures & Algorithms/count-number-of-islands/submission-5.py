class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        ROWS = len(grid)
        COLS = len(grid[0])

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
                q.append((r + 1, c))
                q.append((r - 1, c))
                q.append((r, c + 1))
                q.append((r, c - 1))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    bfs(r, c)
                    res += 1
        
        return res
