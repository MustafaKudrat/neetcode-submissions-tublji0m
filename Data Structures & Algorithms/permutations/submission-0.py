class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = set()

        def bt(curList, visited):
            if len(curList) == len(nums):
                res.append(curList[:])
                return
            for i in range(len(nums)):
                if nums[i] in visited:
                    continue
                curList.append(nums[i])
                visited.add(nums[i])
                bt(curList, visited)
                visited.remove(nums[i])
                curList.pop()

        bt([], visited)
        return res