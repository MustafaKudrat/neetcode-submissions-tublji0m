class MedianFinder:

    def __init__(self):
        self.smallHalf = []
        self.largeHalf = []

    def addNum(self, num: int) -> None:
        if len(self.smallHalf) > 0 and num < -self.smallHalf[0]:
            heapq.heappush(self.smallHalf, -num)
        else:
            heapq.heappush(self.largeHalf, num)
        
        if len(self.smallHalf) - len(self.largeHalf) > 1:
            heapq.heappush(self.largeHalf, -heapq.heappop(self.smallHalf))
        elif len(self.largeHalf) - len(self.smallHalf) > 1:
            heapq.heappush(self.smallHalf, -heapq.heappop(self.largeHalf))


    def findMedian(self) -> float:
        if len(self.smallHalf) > len(self.largeHalf):
            return -self.smallHalf[0]
        elif len(self.smallHalf) < len(self.largeHalf):
            return self.largeHalf[0]
        else:
            return (-self.smallHalf[0] + self.largeHalf[0]) / 2
        