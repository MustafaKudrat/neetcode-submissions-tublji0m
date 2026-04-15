class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # BFS 8 dir
        # Queue (r, c, length)
        # return if r = n - 1 and c = n - 1

        q = deque([(0, 0, 1)])
        visited = set((0, 0))
        direction = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1],[-1, -1]]
        while q:
            r, c, length = q.popleft()
            if r == len(grid) - 1 and c == len(grid) - 1:
                    return length
            if min(r, c) < 0 or max(r, c) >= len(grid) or grid[r][c] == 1:
                continue
            for dr, dc in direction:
                if (r + dr, c + dc) not in visited:
                    q.append((r + dr, c + dc, length + 1))
                    visited.add((r + dr, c + dc))

        return -1

