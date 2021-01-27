class Solution:
    def __init__(self):
        self.solution = set()
    
    def branch(self, S, current):
        if current == len(S):
            self.solution.add(S)
            return
        
        i, j = list(S), list(S)
        i[current] = i[current].upper()
        j[current] = j[current].lower()
        self.branch(''.join(i), current + 1)
        self.branch(''.join(j), current + 1)
    
    def letterCasePermutation(self, S: str) -> List[str]:
        self.branch(S, 0)
        return list(self.solution)