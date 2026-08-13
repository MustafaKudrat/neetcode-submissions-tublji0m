class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        res = 0

        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        visited = set()

        def dfs(n):
            if n in visited:
                return
            visited.add(n)
            for nei in graph[n]:
                dfs(nei)
        
        for i in range(n):
            if i not in visited:
                dfs(i)
                res += 1
        return res