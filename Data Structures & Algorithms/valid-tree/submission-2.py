class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)

        visited = set()

        def dfs(cur, parent):
            if cur in visited:
                return False
            visited.add(cur)
            for nei in graph[cur]:
                if nei == parent:
                    continue
                if not dfs(nei, cur):
                    return False
            return True

        if not dfs(0, -1):
            return False
        
        return len(visited) == n
