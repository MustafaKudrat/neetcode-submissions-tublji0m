class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #  4 3 8 1 4 7 0
        curMin = prices[0]
        res = 0
        for p in prices[1:]:
            res = max(res, p - curMin)
            curMin = min(curMin, p)

        return res
