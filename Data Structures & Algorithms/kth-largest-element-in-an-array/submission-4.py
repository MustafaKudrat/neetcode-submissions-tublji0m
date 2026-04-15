class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        '''
        2 4 1 8 5
        '''
        for i in range(k):
            heapq.heappush(heap, nums[i])
        
        for i in range(k, len(nums)):
            if nums[i] > heap[0]:
                heapq.heappushpop(heap, nums[i])
        
        return heap[0]