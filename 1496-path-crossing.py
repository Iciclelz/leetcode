class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set()
        cc = (0, 0)
        visited.add(cc)
        
        for x in path:
            if x == 'N':
                cc = (cc[0] + 1, cc[1])
            
            if x == 'S':
                cc = (cc[0] - 1, cc[1])
            
            if x == 'E':
                cc = (cc[0], cc[1] + 1)
            
            if x == 'W':
                cc = (cc[0], cc[1] - 1)
            
            if cc in visited:
                return True
        
            visited.add(cc)
        
        return False
            