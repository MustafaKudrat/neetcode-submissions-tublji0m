class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # 1 2 2 3 3 3
        # freq: 1:1 2:2 3:3
        # freqVK: 1:[1], 2:[2], 3:[3]
        count = Counter(nums)
        freq = defaultdict(list)
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        res = []
        for i in range(len(nums), 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
