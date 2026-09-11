class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapper = defaultdict(list)
        for s in strs:
            counter = [0] * 26
            for c in s:
                counter[ord(c) - ord('a')] += 1
            mapper[tuple(counter)].append(s)
        
        res = []
        for v in mapper.values():
            res.append(v)
        
        return res