class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMin, curMax = 1, 1
        res = float('-inf')
        cur = 1
        for num in nums:
            cur = curMax * num
            curMax = max(curMax * num, curMin * num, num, cur)
            curMin = min(cur, curMin * num, num, cur)

            res = max(res, curMax)
        
        return res
        
        