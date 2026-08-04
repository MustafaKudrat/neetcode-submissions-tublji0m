class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        curList = []
        candidates.sort()
        def dfs(i, curSum):
            if curSum == target:
                res.append(curList[:])
                return

            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                if curSum + candidates[j] > target:
                    break
                curList.append(candidates[j])
                dfs(j + 1, curSum + candidates[j])
                curList.pop()
        dfs(0, 0)
        return res
            