class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for st in stones:
            heapq.heappush(heap, -st)
        
        while len(heap) > 1:
            st1, st2 = -heapq.heappop(heap), -heapq.heappop(heap)
            if st1 != st2:
                heapq.heappush(heap, -abs(st1 - st2))
            
        return -heap[0] if heap else 0