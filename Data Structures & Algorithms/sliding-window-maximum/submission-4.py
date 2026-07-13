class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxHeap = []
        for i in range(k):
            heapq.heappush(maxHeap, (-nums[i], i))
        
        # 1,0 2,1 1,2
        res = []
        res.append(-maxHeap[0][0])
        for j in range(k, len(nums)):
            heapq.heappush(maxHeap, (-nums[j], j))
            curVal, curIdx = maxHeap[0]
            while j - curIdx >= k:
                curVal, curIdx = heapq.heappop(maxHeap)
            heapq.heappush(maxHeap, (curVal, curIdx))
            res.append(-curVal)

        return res