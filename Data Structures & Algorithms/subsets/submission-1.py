class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curset = []

        def dfs(i, curset):
            if i >= len(nums):
                res.append(curset[:])
                return

            curset.append(nums[i])
            dfs(i+1, curset)

            curset.pop()
            dfs(i+1, curset)

        dfs(0,[])

        return res