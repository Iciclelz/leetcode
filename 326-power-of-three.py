class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while not n % 3 and n > 1:
            n //= 3
            
        return n == 1;