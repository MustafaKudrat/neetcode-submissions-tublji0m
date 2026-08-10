class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r, c])
                    visited.add((r, c))

        def move(r, c):
            if (min(r, c) < 0 or r == ROWS or c == COLS or
            grid[r][c] == 0 or (r, c) in visited):
                return
            q.append([r, c])
            visited.add((r, c))

        day = 0

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = 2

                move(r + 1, c)
                move(r - 1, c)
                move(r, c + 1)
                move(r, c - 1)
            day += 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
        return max(0, day - 1)

        


