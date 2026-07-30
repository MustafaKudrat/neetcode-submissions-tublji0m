class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        counter = Counter(nums)
        bucket = defaultdict(list)
        for val, cnt in counter.items():
            bucket[cnt].append(val)

        for i in range(len(nums), -1, -1):
            if i in bucket:
                for item in bucket[i]:
                    res.append(item)
                    if len(res) == k:
                        return res
        
        return []