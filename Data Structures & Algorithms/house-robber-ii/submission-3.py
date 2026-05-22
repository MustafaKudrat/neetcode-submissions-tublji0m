class Solution:
    def rob(self, nums: List[int]) -> int:
        # nums[:-1]
        # or nums[1:]
        if len(nums) < 2:
            return nums[0]
        rob1, rob2 = 0, 0
        for num in nums[:len(nums) - 1]:
            tmp = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = tmp
        res1 = rob2
        rob1, rob2 = 0, 0
        for num in nums[1:]:
            tmp = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = tmp
        return max(res1, rob2)