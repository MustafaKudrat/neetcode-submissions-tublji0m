class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        maxHeap = []
        for key, v in counter.items():
            heapq.heappush(maxHeap, (v, key))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        res = []
        while maxHeap:
            cnt, val = heapq.heappop(maxHeap)
            res.append(val)
        
        return res