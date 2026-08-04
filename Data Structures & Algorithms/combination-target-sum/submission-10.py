class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curList = []
        nums.sort()
        def dfs(i, curSum):
            if i == len(nums) or curSum > target:
                return
            if curSum == target:
                res.append(curList[:])

            for j in range(i, len(nums)):
                curList.append(nums[j])
                dfs(j, curSum + nums[j])
                curList.pop()
        dfs(0, 0)
        return res
            