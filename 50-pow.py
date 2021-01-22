class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n > 0:
            while n % 2 == 0:
                n //= 2
                x *= x
            if n == 1:
                return x
            else:
                return x * self.myPow(x, n - 1)
        else:
            return 1 / self.myPow(x, abs(n))
            
            