class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        nodeMap = defaultdict(list)
        for v1, v2 in edges:
            nodeMap[v1].append(v2)
            nodeMap[v2].append(v1)
        
        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)
            for nei in nodeMap[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            return True

        if not dfs(0, -1):
            return False
        
        return len(visited) == n