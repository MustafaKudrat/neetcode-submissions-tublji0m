class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # djikstra algo

        res = 0
        edges = defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))
        visited = set()
        minHeap = [(0, k)] #(weight, node)

        while minHeap:
            curWeight, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            
            visited.add(node)
            if len(visited) == n:
                return curWeight

            for nei, wei in edges[node]:
                if nei in visited:
                    continue
                heapq.heappush(minHeap, (curWeight + wei, nei))
        return -1