class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)

        curL = 1
        for i in range(len(nums)):
            curL *= nums[i]
            left[i] = curL
        
        curR = 1
        for j in range(len(nums) - 1, -1, -1):
            curR *= nums[j]
            right[j] = curR
        
        res = []
        for i in range(len(nums)):
            if i == 0:
                res.append(right[i + 1])
            elif i == len(nums) - 1:
                res.append(left[i - 1])
            else:
                res.append(left[i - 1] * right[i + 1])
        return res