class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        
        maxNum = []
        for s in stones:
            maxNum.append(-s)
        heapq.heapify(maxNum)

        while len(maxNum) > 2:
            first = heapq.heappop(maxNum)
            second = heapq.heappop(maxNum)
            if first == second:
                continue
            elif first < second:
                heapq.heappush(maxNum, first - second)
            else:
                heapq.heappush(maxNum, second - first)

        if len(maxNum) == 1:
            return -maxNum[0]
        first = heapq.heappop(maxNum)
        second = heapq.heappop(maxNum)
        if first == second:
            return 0
        elif first < second:
            return second - first
        else:
            return first - second
        
