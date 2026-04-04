class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            # 1 & 2. Base Cases: Out of bounds OR water
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
                return
            
            # 3. Mark as visited (sink the island)
            grid[r][c] = '0'
            
            # 4. Explore all 4 adjacent directions
            dfs(r - 1, c) # Up
            dfs(r + 1, c) # Down
            dfs(r, c - 1) # Left
            dfs(r, c + 1) # Right

        # The Outer Loop
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':  # Found unvisited land
                    islands += 1
                    dfs(r, c)          # Sink the entire island

        return islands
        