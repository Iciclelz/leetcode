import math
import queue

class Solution:
    def vertices(self):
        return [(x, y) for y in range(len(self.grid[0])) for x in range(len(self.grid))]

    def adjacent(self, u):
        l = list()

        if u[0] + 1 < len(self.grid):
            l.append((u[0] + 1, u[1]))

        if u[1] + 1 < len(self.grid[0]):
            l.append((u[0], u[1] + 1))
        
        return l

    def length(self, u, v):
        return self.grid[v[0]][v[1]]

    def dijkstra(self, s, u):
        distance = dict()
        pq = queue.PriorityQueue()

        distance[s] = 0
        pq.put((distance[s], s))

        for v in self.vertices():
            if v != s:
                distance[v] = math.inf

        while not pq.empty():
            _, u = pq.get()
            for v in self.adjacent(u):
                if distance[v] > distance[u] + self.length(u, v):
                    distance[v] = distance[u] + self.length(u, v)
                    pq.put((distance[v], v))
            
        return distance
    
    def minPathSum(self, grid: List[List[int]]) -> int:
        self.grid = grid
        
        start = (0,0)
        end = (len(grid)-1, len(grid[0])-1)
        
        distance = self.dijkstra(start, end)
        
        # distance at end + initial cost
        return distance[end] + grid[0][0]