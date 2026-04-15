class Solution:
    from collections import deque

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:


        output = []
        q = deque()  # stores indices, not values
        l = r = 0

        while r < len(nums):
            # Pop smaller values from the end
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # Remove left index if it's out of the window
            if q[0] < l:
                q.popleft()

            # Add to output once we have a full window
            if r + 1 >= k:
                output.append(nums[q[0]])
                l += 1

            r += 1

        return output
