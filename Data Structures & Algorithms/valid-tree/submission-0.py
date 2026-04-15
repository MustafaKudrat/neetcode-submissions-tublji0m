class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False  # A tree must have exactly n - 1 edges
        
        # map the nodes to edges
        mapping = {i:[] for i in range(n)}
        for first, last in edges:
            mapping[first].append(last)
            mapping[last].append(first)

        visited = set()

        # dfs to detect cycle
        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)
            for neighbor in mapping[node]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, node):
                    return False
            return True

        # Start DFS from node 0
        if not dfs(0, -1):
            return False

        # Ensure all nodes are connected
        return len(visited) == n