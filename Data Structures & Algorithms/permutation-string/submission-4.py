class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter1 = {}
        for c in s1:
            counter1[c] = 1 + counter1.get(c, 0)
        
        need = len(counter1)

        for i in range(len(s2)):
            counter2 = {}
            have = 0
            for j in range(i, len(s2)):
                counter2[s2[j]] = 1 + counter2.get(s2[j], 0)
                if counter2[s2[j]] > counter1.get(s2[j], 0):
                    break
                if counter2[s2[j]] == counter1.get(s2[j], 0):
                    have += 1
                if have == need:
                    return True

        return False