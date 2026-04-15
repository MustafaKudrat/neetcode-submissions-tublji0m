class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        sort
        traverse each
            if nums[i] > 0:
                return
            else: 
                do 2 pointer check for -nums[i] for i + 1 : end
                while l < r:
                    if nums[l] + nums[r] < nums[i]:
                        l += 1
                    elif >:
                        r -= 1
                    else:
                        add i,l,r to res
                        update l r
                        while l == l-1 and l < r:
                            l += 1

            
        '''
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break
            l, r = i + 1, len(nums) - 1
            while l < r:
                cur = nums[i] + nums[l] + nums[r]
                if cur < 0:
                    l += 1
                elif cur > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res








