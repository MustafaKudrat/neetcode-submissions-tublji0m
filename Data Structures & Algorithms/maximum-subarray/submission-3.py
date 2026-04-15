class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = -float('inf')
        for i in range(len(nums)):
            for j in range(i, len(nums)+1):
                curSum = sum(nums[i:j+1])
                maxSum = max(maxSum, curSum)

        return maxSum if maxSum != -float('inf') else nums[0]
