class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for num in nums:
            if num in hashMap:
                hashMap[num] += 1
            else:
                hashMap[num] = 1
        
        ordered = sorted(hashMap.items(), key=lambda item:item[1], reverse=True)

        sortedDict = dict(ordered)

        return list(sortedDict.keys())[:k]
