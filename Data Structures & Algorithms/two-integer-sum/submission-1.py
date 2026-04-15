class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sortedNum = []
        for i, num in enumerate(nums):
            sortedNum.append([num,i])

        sortedNum.sort()
        # [3,0], [4,1], [5,2], [6,3]
        l, r = 0, len(nums) - 1
        while l < r:
            if sortedNum[l][0] + sortedNum[r][0] > target:
                r -= 1
            elif sortedNum[l][0] + sortedNum[r][0] < target:
                l += 1
            else:
                return [min(sortedNum[l][1], sortedNum[r][1]), max(sortedNum[l][1], sortedNum[r][1])]

        
