class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combo = []
        nums.sort()

        def dfs(i, curSum):
            if curSum == target:
                res.append(combo[:])
                return

            if i == len(nums) or curSum > target:
                return
            
            combo.append(nums[i])
            dfs(i, curSum + nums[i])
            combo.pop()
            dfs(i + 1, curSum)

        dfs(0, 0)
        return res
