class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        freq = defaultdict(list)

        for num, cnt in counter.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(nums), -1, -1):
            if freq[i] != 0:
                for num in freq[i]:
                    res.append(num)
                    if len(res) == k:
                        return res
        return res
