class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(curIdx,curSum,curList):
            if curIdx >= len(nums) or curSum > target:
                return
            if curSum == target:
                res.append(curList.copy())
                return
            # take cur
            curList.append(nums[curIdx])
            dfs(curIdx, curSum + nums[curIdx], curList)

            # don't take cur
            curList.pop()
            dfs(curIdx + 1, curSum, curList)

        dfs(0, 0, [])
        return res