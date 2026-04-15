class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #abc
        #aacbbcba
        
        n = len(s1)
        newS1 = sorted(s1)

        for  i in range(len(s2) - n + 1):
            if sorted(s2[i: i + n]) == newS1:
                return True

            
        return False