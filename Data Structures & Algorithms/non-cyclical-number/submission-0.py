class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = self.sumOfSquares(n)
        return True

    def sumOfSquares(self, n):
        res = 0
        while n:
            cur = n % 10
            cur = cur ** 2
            res += cur
            n = n // 10
        
        return res