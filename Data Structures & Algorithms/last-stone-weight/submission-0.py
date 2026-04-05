import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Convert all stones to negative values to simulate a Max-Heap
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        
        # Continue smashing while there is more than 1 stone left
        while len(max_heap) > 1:
            # Pop the two "heaviest" stones (smallest negative numbers)
            stone1 = heapq.heappop(max_heap)
            stone2 = heapq.heappop(max_heap)
            
            # If they are not equal, push the remaining weight back
            # Since both are negative, stone1 <= stone2. 
            # The difference in absolute weights is (stone2 - stone1).
            # To push it back as a negative value, we just do stone1 - stone2.
            if stone1 != stone2:
                heapq.heappush(max_heap, stone1 - stone2)
                
        # If the heap is empty, return 0. Otherwise, return the positive weight of the last stone.
        return -max_heap[0] if max_heap else 0