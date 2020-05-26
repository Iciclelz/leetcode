class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        sequences = dict()
        
        n = 0
        
        for x in range(len(s) - 9):
            sequence = s[n:n+10]
            if sequence in sequences:
                sequences[sequence] += 1
            else:
                sequences[sequence] = 1
            n += 1
        
        return list(map(lambda k : k[0], filter(lambda k : k[1] > 1, sequences.items())))