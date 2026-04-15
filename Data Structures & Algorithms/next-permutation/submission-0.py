class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        find first dip form right
        if no dip, return reverse
        find next larger number to the right
        swap first dip with next larger number to the right
        in place reverse dip + 1 to end
        '''

        valley = - 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                valley = i
                break

        if valley == -1:
            nums.reverse()
            return

        nextLarger = len(nums) - 1
        while nums[nextLarger] <= nums[valley]:
            nextLarger -= 1

        nums[valley], nums[nextLarger] = nums[nextLarger], nums[valley]

        # in place reverse
        l, r = valley + 1, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        

        