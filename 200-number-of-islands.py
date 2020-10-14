class Solution:
    
    def purge(self, grid, coordinate):
        x,y = coordinate
        
        grid[x][y] = '0'
        
        # purge north
        if x - 1 >= 0 and grid[x - 1][y] == '1':
            self.purge(grid, (x - 1, y))
        
        # purge south
        if x + 1 < len(grid) and grid[x + 1][y] == '1':
            self.purge(grid, (x + 1, y))
        
        # purge left
        if y - 1 >= 0 and grid[x][y - 1] == '1':
            self.purge(grid, (x, y - 1))
        
        #purge right
        if y + 1 < len(grid[x]) and grid[x][y + 1] == '1':
            self.purge(grid, (x, y + 1))
        
        
        
    
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        mask = list()
        
        for n in range(len(grid)):
            l = list()
            for m in range(len(grid[n])):
                l.append(grid[n][m])
            mask.append(l)
        
        for n in range(len(mask)):
            for m in range(len(mask[n])):
                if mask[n][m] == '1':
                    islands += 1
                    self.purge(mask, (n, m))
        
        return islands
