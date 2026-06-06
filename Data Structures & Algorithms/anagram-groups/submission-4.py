class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for strr in strs:
            counter = [0] * 26
            for c in strr:
                counter[ord(c) - ord('a')] += 1
            res[tuple(counter)].append(strr)

        return list(res.values())