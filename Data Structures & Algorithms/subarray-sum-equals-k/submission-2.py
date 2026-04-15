class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = defaultdict(int)
        prefixSum[0] = 1
        res = 0
        curSum = 0

        for num in nums:
            curSum += num
            res += prefixSum[curSum-k]
            prefixSum[curSum] += 1
        return res