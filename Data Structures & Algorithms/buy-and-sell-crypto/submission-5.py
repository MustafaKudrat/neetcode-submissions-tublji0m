class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i, len(prices)):
                res = max(res, prices[j] - buy)

        return res