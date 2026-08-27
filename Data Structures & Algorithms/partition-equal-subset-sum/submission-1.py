class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2

        dp = set()
        dp.add(0)

        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            for j in dp:
                if j + nums[i] == target:
                    return True
                nextDP.add(j)
                nextDP.add(j + nums[i])

            dp = nextDP
        
        return False