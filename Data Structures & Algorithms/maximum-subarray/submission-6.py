class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0
        for num in nums:
            curSum += num
            # !!!!!
            # MUST UPDATE MAXSUM FIRST CUZ [-2]
            if maxSum < curSum:
                maxSum = curSum
            if curSum < 0:
                curSum = 0
        return maxSum