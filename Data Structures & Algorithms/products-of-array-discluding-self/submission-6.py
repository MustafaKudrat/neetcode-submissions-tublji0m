class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProduct = [1]
        rightProduct = [1]

        for num in nums:
            leftProduct.append(leftProduct[-1] * num)
        
        for i in range(len(nums) - 1, -1, -1):
            rightProduct.append(rightProduct[-1] * nums[i])
        
        res = []
        for i in range(len(nums)):
            res.append(leftProduct[i] * rightProduct[-2 - i])
        
        return res