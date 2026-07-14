class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()
        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if r - q[0] >= k:
                q.popleft()

            if r + 1 >= k:
                res.append(nums[q[0]])
        return res
