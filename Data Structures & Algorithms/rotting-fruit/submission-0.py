import collections

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        queue = collections.deque()
        fresh_count = 0

        # 1. INITIALIZATION: Find sources AND count the targets
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1

        # Edge case: If there are zero fresh oranges to begin with, it takes 0 mins.
        if fresh_count == 0:
            return 0

        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        mins = 0

        # 2. LEVEL-BY-LEVEL BFS
        # We only continue if the queue has items AND there are still fresh oranges left
        while queue and fresh_count > 0:
            # We are entering a new minute
            mins += 1 
            
            # Process exactly the number of items currently in this level (minute)
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in direction:
                    nr, nc = r + dr, c + dc

                    # If we find a fresh orange
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2        # Rot it
                        fresh_count -= 1        # Check it off our list
                        queue.append((nr, nc))  # Queue it to rot its neighbors NEXT minute

        # 3. THE DISCONNECT CHECK
        if fresh_count == 0:
            return mins
        else:
            return -1