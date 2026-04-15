class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 2  5  5 1 6  target = 3
# dict.  2:0 5:1 5:2 
        seen = {}
        for i, num in enumerate(nums):
            if (target - num) in seen:
                return [seen[target - num], i]
            seen[num] = i
        #return [0, 0]