class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #maxHeap - nlogk S: n
        #counter -> frequencyList - n S:2n

        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        heap = []
        for num in freq.keys():
            heapq.heappush(heap, (freq[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        while heap:
            res.append(heapq.heappop(heap)[1])

        return res