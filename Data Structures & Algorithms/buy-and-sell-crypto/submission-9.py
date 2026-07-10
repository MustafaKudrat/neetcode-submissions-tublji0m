class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, res = prices[0], 0
        for p in prices:
            if p < buy:
                buy = p
            if p > buy:
                res = max(res, p - buy)
        return res