class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        if not heights:
            return []

        rows, cols = len(heights), len(heights[0])
        pac_reachable = set()
        atl_reachable = set()

        def dfs(r, c, visit_set, prev_height):
            # 1. Base cases for boundaries, already visited, or invalid height
            if (r < 0 or r >= rows or 
                c < 0 or c >= cols or 
                (r, c) in visit_set or 
                heights[r][c] < prev_height): # Enforce "flow uphill"
                return

            # 2. Mark as reachable from this ocean
            visit_set.add((r, c))

            # 3. Explore all 4 neighbors, passing the current height as the new prev_height
            dfs(r + 1, c, visit_set, heights[r][c])
            dfs(r - 1, c, visit_set, heights[r][c])
            dfs(r, c + 1, visit_set, heights[r][c])
            dfs(r, c - 1, visit_set, heights[r][c])

        # 1. Run DFS from the Pacific borders (Top and Left)
        for c in range(cols):
            dfs(0, c, pac_reachable, heights[0][c])        # Top Row
        for r in range(rows):
            dfs(r, 0, pac_reachable, heights[r][0])        # Left Col

        # 2. Run DFS from the Atlantic borders (Bottom and Right)
        for c in range(cols):
            dfs(rows - 1, c, atl_reachable, heights[rows - 1][c]) # Bottom Row
        for r in range(rows):
            dfs(r, cols - 1, atl_reachable, heights[r][cols - 1]) # Right Col

        # 3. Find the Intersection
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac_reachable and (r, c) in atl_reachable:
                    res.append([r, c])

        return res