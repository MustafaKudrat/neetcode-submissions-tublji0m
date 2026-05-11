class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        DIRECTIONS = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        ROWS = len(grid)
        COLS = len(grid[0])
        res = 0

        def bfs(row, col):
            q = deque()
            grid[row][col] = '0'
            q.append((row, col))

            while q:
                row, col = q.popleft()
                for dr, dc in DIRECTIONS:
                    r = row + dr
                    c = col + dc
                    if (r in range(ROWS) and c in range(COLS) and grid[r][c] != '0'):
                        q.append((r, c))
                        grid[r][c] = '0'
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    bfs(r, c)
                    res += 1
        
        return res
