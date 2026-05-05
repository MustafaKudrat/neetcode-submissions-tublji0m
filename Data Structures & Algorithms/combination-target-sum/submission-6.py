class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(curIdx,curSum,curList):
            if curSum == target:
                res.append(curList.copy())
                return
            
            for j in range(curIdx, len(nums)):
                if curSum + nums[j] > target:
                    return
                curList.append(nums[j])
                dfs(j, curSum + nums[j], curList)
                curList.pop()

        dfs(0, 0, [])
        return res