class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        m=len(word1) + 1
        n=len(word2) + 1
        
        d = {}
        for i in range(m):
            d[i, 0] = i
        
        for j in range(n):
            d[0, j] = j
        
        for j in range(1, n):
            for i in range(1, m):
                cost = 0 if word1[i-1] == word2[j-1] else 1
                d[i, j] = min([
                    d[i-1, j] + 1,       # deletion
                    d[i, j-1] + 1,       # insertion
                    d[i-1, j-1] + cost   # substitution
                ])

        return d[m-1, n-1]