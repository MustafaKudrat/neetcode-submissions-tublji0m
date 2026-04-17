class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 3 2 4 1  2
        # 1 3 6 24 24
        #   8  2 2 1
        lProduct = [1]
        rProduct = [1] * len(nums)
        # left to right
        for num in nums:
            lProduct.append(lProduct[-1] * num)
        for j in range(len(nums) - 2, -1, -1):
            rProduct[j] = rProduct[j + 1] * nums[j + 1]
        res = []
        for pos in range(len(nums)):
            res.append(lProduct[pos] * rProduct[pos])
        return res