import collections

class Solution:
    def islandsAndTreasure(self, grid: list[list[int]]) -> None:
        if not grid:
            return
            
        rows, cols = len(grid), len(grid[0])
        queue = collections.deque()
        
        # 1. MULTI-SOURCE INITIALIZATION
        # Find ALL treasures and put them in the queue at Level 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        INF = 2147483647
        
        # 2. THE SIMULTANEOUS BFS
        while queue:
            r, c = queue.popleft()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check bounds AND check if the cell is unvisited land (INF)
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == INF:
                    # The distance is just the current cell's distance + 1!
                    grid[nr][nc] = grid[r][c] + 1
                    
                    # Add the newly reached land to the queue to continue the ripples
                    queue.append((nr, nc))