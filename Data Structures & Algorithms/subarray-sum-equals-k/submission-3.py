class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pref = defaultdict(int)
        pref[0] = 1
        curSum = 0
        res = 0

        for i in range(len(nums)):
            curSum += nums[i]
            res += pref[curSum - k]
            pref[curSum] += 1

        return res