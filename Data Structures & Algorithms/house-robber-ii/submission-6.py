class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.robHelper(nums[1:]), self.robHelper(nums[:-1]))
    
    def robHelper(self, nums):
        rob1, rob2 = 0, 0

        for num in nums:
            tmp = rob2
            rob2 = max(num + rob1, rob2)
            rob1 = tmp
        
        return rob2