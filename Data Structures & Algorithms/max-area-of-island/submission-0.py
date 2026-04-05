class Solution:
    def dfs(self, grid, i, j):
        # 1. BASE CASE: If out of bounds OR if it's water, the area here is 0.
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
            return 0

        # 2. MARK VISITED: Sink the island so we don't count it twice
        grid[i][j] = 0

        # 3. CALCULATE AREA: Current land (1) + all connected land
        area = 1
        area += self.dfs(grid, i - 1, j) # Up
        area += self.dfs(grid, i + 1, j) # Down
        area += self.dfs(grid, i, j + 1) # Right
        area += self.dfs(grid, i, j - 1) # Left
        
        return area

    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        max_area = 0
        rows, cols = len(grid), len(grid[0])

        for i in range(rows):
            for j in range(cols):
                # Only run DFS if we find land!
                if grid[i][j] == 1:
                    current_area = self.dfs(grid, i, j)
                    max_area = max(max_area, current_area)

        # Make sure to return max_area, not the local loop area
        return max_area