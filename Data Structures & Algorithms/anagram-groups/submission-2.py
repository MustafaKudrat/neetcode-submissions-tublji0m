class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # counter has to be [0] * 26
        
        res = defaultdict(list)
        
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)

        return list(res.values())