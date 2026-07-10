class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell, res = prices[0], prices[0], 0
        for p in prices:
            if p < buy:
                buy = p
            if p > buy:
                sell = p
                res = max(res, sell - buy)
        return res