class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = max(piles)
        while l <= r:
            mid = (l + r) // 2
            time = sum([math.ceil(p / mid) for p in piles])
            if time <= h:
                res = mid
                r = mid - 1
            elif time > h:
                l = mid + 1
        return res