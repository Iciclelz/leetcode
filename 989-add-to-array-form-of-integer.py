class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        
        B = []
        k = str(int(''.join(map(lambda x : str(x), A))) + K)
        for x in range(len(k)):
            B.append(int(k[x]))
        
        return B