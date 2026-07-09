class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                return res
            target = -nums[i]
            for n1, n2 in self.twoSum(nums, i + 1, target):
                res.append([nums[i], n1, n2])
        return res
            
    def twoSum(self, nums, start, target):
        l, r = start, len(nums) - 1
        res = []
        while l < r:
            curSum = nums[l] + nums[r]
            if curSum < target:
                l += 1
            elif curSum > target:
                r -= 1
            else:
                res.append([nums[l], nums[r]])
                l += 1
                r -= 1
            
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1
        return res