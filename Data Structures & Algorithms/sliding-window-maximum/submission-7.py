class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()
        for r in range(len(nums)):
            while q and q[-1][0] < nums[r]:
                q.pop()
            q.append((nums[r], r))

            if r - q[0][1] >= k:
                q.popleft()

            if r + 1 >= k:
                res.append(q[0][0])
        return res
