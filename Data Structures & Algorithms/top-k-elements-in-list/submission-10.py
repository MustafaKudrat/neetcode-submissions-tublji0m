class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #maxHeap - nlogk S: n
        #counter -> frequencyList - n S:2n

        counter = Counter(nums)
        freq = defaultdict(list)
        for key, val in counter.items():
            freq[val].append(key)
        
        res = []
        for i in range(len(nums), -1, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
        return res