import bisect
import random
class Solution:
    def __init__(self, w: List[int]):
        curSum = 0
        self.pref = []
        # 1 3 2
        # 1 4 6
        for x in w:
            curSum += x
            self.pref.append(curSum)
        self.total = curSum

    def pickIndex(self) -> int:
        randNum = random.randint(1, self.total)
        return bisect.bisect_left(self.pref, randNum)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()