class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        res = []
        for strr in strs:
            counter = [0] * 26
            for c in strr:
                counter[ord(c) - ord('a')] += 1
            group[tuple(counter)].append(strr)
        
        for k, v in group.items():
            res.append(v)

        return res