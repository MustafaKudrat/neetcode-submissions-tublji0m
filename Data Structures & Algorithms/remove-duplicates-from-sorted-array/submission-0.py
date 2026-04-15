class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        0 1 2 3 2 3
              l
                  r
        0 0 0 0
          l
               r
        1 2 3 4
               l
               r
        
        '''
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1

        return l