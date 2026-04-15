class Solution:

    from collections import Counter
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #abc
        #aacbbcba

        n = len(s1)

        if n > len(s2):
            return False

        c1 = Counter(s1)
        c2 = Counter(s2[:n])

        if c1 == c2:
            return True

        for i in range(n, len(s2)):
            c2[s2[i]] += 1
            c2[s2[i-n]] -= 1

            if c2[s2[i-n]] == 0:
                del c2[s2[i-n]]
            if c1 == c2:
                return True

        return False
