class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, curComb, total):
            if total == target:
                res.append(curComb[:])
                return
            
            if i >= len(candidates) or total > target:
                return


            # Include i
            curComb.append(candidates[i])
            dfs(i + 1, curComb, total + candidates[i])
            curComb.pop()

            # Not Include i
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i + 1, curComb, total)

        dfs(0, [], 0)
        return res