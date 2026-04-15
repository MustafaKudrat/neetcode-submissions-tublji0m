class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #count = n

        # Step 1: Build adjacency list
        graph = {i: [] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # Step 2: Track visited nodes
        visited = set()

        # Step 3: DFS to mark all connected nodes
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)

        # Step 4: Count components
        count = 0
        for i in range(n):
            if i not in visited:
                count += 1  # New component found
                dfs(i)

        return count