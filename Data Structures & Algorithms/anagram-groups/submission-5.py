class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        anagrams = []
        for st in strs:
            cnt = [0] * 26
            for c in st:
                cnt[ord(c) - ord('a')] += 1
            res[tuple(cnt)].append(st)

        for k, v in res.items():
            anagrams.append(v)

        return anagrams