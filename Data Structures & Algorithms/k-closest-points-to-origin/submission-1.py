class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            dist = abs(math.sqrt((x - 0)**2 + (y - 0)**2))
            heapq.heappush(heap, (-dist, (x, y)))
            if len(heap) > k:
                heapq.heappop(heap)
            
        return [[cord[0], cord[1]] for dist, cord in heap]