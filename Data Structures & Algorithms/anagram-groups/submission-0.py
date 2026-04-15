class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]

        hashTable = {}

        for i in range(0,len(strs)):
            key = str(sorted(strs[i]))
            if key not in hashTable:
                hashTable[key] = []
            hashTable[key].append(strs[i])

        res = []
        for w in hashTable.values():
            res.append(w)

        return res