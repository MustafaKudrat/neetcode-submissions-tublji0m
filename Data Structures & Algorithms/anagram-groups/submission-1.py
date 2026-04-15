class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedDict = defaultdict(list)
        for str in strs:
            key = "".join(sorted(str))
            sortedDict[key].append(str)
        
        return [v for v in sortedDict.values()]