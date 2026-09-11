class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        bucket = defaultdict(list)

        for key, val in counter.items():
            bucket[val].append(key)
        
        res = []
        for i in range(len(nums), -1, -1):
            for num in bucket[i]:
                res.append(num)
            if len(res) == k:
                return res

        return res