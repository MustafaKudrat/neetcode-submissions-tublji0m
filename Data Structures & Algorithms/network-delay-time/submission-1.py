class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # djikstra algo

        graph = defaultdict(list)
        for u, v, t in times:
            graph[u].append((v, t))
        
        minHeap = [(0, k)]
        visited = set()

        while minHeap:
            curWei, node = heapq.heappop(minHeap)
            if node in visited:
                continue
    
            visited.add(node)
            if len(visited) == n:
                return curWei
            #res = max(res, curWei)
            for nei, t in graph[node]:
                if nei not in visited:
                    heapq.heappush(minHeap, (curWei + t, nei))
        
        return -1