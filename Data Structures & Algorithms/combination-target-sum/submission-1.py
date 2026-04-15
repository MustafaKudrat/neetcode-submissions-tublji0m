class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curComb, total):
            if total == target:
                res.append(curComb[:])
                return
            
            if i >= len(candidates) or total > target:
                return

            curComb.append(candidates[i])
            dfs(i, curComb, total + candidates[i])
            curComb.pop()
            dfs(i + 1, curComb, total)

        dfs(0, [], 0)
        return res