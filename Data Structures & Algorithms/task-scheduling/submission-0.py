class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxHeap = [] # -cnt, ava
        count = Counter(tasks)
        for cnt in count.values():
            heapq.heappush(maxHeap, -cnt)
        
        q = deque() # (cnt, availableTime)
        res = 0
        while maxHeap or q:
            res += 1

            if not maxHeap:
                res = q[0][1]
                #return q[-1][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt < 0:
                    q.append([cnt, res + n])
            if q and q[0][1] == res:
                heapq.heappush(maxHeap, q.popleft()[0])
        return res