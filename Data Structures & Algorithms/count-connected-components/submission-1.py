class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # adjency list
        nodeMap = defaultdict(list)
        for n1, n2 in edges:
            nodeMap[n1].append(n2)
            nodeMap[n2].append(n1)

        # dfs
        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nei in nodeMap[node]:
                dfs(nei)

        # loop thru nodes with dfs
        res = 0
        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i)

        return res