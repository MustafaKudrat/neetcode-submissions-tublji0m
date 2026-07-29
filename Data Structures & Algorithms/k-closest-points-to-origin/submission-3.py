class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            dist = abs(x*x + y*y)
            heapq.heappush(heap, (-dist, (x, y)))
            if len(heap) > k:
                heapq.heappop(heap)
            
        return [[cord[0], cord[1]] for dist, cord in heap]