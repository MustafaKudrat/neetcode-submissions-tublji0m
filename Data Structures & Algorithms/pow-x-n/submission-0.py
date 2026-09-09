class Solution:
    def myPow(self, x: float, n: int) -> float:
        def getPower(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            
            res = getPower(x, n // 2)
            res *= res
            res = res * x if n % 2 else res
            return res

        res = getPower(x, abs(n))
        return res if n > 0 else 1 / res
