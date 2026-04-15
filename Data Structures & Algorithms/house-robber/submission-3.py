class Solution:
    def rob(self, nums: List[int]) -> int:
        # 1 2 (3 4 5)
        # _ 2 ()
        if len(nums) < 2:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(nums[i]+dp[i-2], dp[i-1])

        print(dp)
        return dp[-1]
