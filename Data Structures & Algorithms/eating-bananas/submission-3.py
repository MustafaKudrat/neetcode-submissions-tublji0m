class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = max(piles)
        while l <= r:
            mid = (l + r) // 2
            time = self.timeToFinish(piles, mid)
            if time <= h:
                res = mid
                r = mid - 1
            elif time > h:
                l = mid + 1
        return res

    def timeToFinish(self, piles, k):
        res = 0
        for p in piles:
            res += math.ceil(p / k)
        return res