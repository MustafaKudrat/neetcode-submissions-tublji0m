class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 1 2 0 1 0
        goal = len(nums) - 1
        i = len(nums) - 2
        while i >= 0:
            if i + nums[i] >= goal:
                goal = i
            i -= 1

        return goal <= 0

