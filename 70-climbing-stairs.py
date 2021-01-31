class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n

        cache = [None] * n
        cache[0], cache[1], cache[2] = 1, 2, 3
        for x in range(3, n):
            cache[x] = cache[x-1] + cache[x-2]
        return cache[n-1]