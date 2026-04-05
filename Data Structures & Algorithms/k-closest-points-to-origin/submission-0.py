import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        
        for x, y in points:
            # Calculate the squared distance
            dist = (x ** 2) + (y ** 2)
            
            # Push the negative distance to simulate a Max-Heap
            # We also store the original point coordinates
            heapq.heappush(max_heap, (-dist, [x, y]))
            
            # If our club gets too full, kick out the "farthest" point (which is at the top)
            if len(max_heap) > k:
                heapq.heappop(max_heap)
                
        # The heap now contains the k closest points. 
        # Extract just the coordinates to return them.
        return [point for dist, point in max_heap]