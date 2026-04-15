class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')

        l = 0
        # 2 3 4 1 2 target: 7
        curSum = 0
        for r in range(len(nums)):
            curSum += nums[r]
            while l <= r and curSum >= target:
                res = min(res, r - l + 1)
                curSum -= nums[l]
                l += 1
            r += 1

        return res if res < float('inf') else 0