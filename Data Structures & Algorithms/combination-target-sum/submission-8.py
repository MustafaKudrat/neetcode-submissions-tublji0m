class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combo = []
        nums.sort()

        def dfs(i, curSum):
            if curSum == target:
                res.append(combo[:])
                return
            
            for j in range(i, len(nums)):
                if curSum + nums[j] > target:
                    return
                combo.append(nums[j])
                dfs(j, curSum + nums[j])
                combo.pop()

        dfs(0, 0)
        return res
