class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            dis = math.sqrt((point[0] - 0) ** 2 + (point[1] - 0) ** 2)
            heap.append((dis, point))

        heapq.heapify(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res