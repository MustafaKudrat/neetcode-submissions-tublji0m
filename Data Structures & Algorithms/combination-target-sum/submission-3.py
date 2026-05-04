class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curList, curSum):
            if curSum == target:
                res.append(curList.copy())
                return 
            if i >= len(nums) or curSum > target:
                return
            
            curList.append(nums[i])
            dfs(i, curList, curSum + nums[i])
            curList.pop()
            dfs(i + 1, curList, curSum)

        dfs(0, [], 0)

        return res