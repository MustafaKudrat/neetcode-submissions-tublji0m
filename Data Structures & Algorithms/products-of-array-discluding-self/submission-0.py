class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
#prefix: product of all before curr index
#postfix: product of all after curr index
#res[i]: prefix[i]*postfix[i]

        res = [1] * len(nums)
        prefix = 1

        #left to right to get prefix for each position
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        print(res)

        #right to left to get postfix
        postfix = 1
        for j in range(len(nums) - 1, -1, -1):
            res[j] *= postfix    
            postfix *= nums[j]
        return res