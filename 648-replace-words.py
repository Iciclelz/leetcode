class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        v = sentence.split(' ')
        
        for x in range(len(v)):
            for z in dict:
                if v[x].startswith(z):
                    v[x] = z
        
        return ' '.join(v)