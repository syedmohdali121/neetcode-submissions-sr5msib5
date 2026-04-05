import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = nums
        
        # Transform the initial list into a valid min-heap in O(N) time
        heapq.heapify(self.min_heap)
        
        # If the heap has more than k elements, pop the smallest ones 
        # until exactly k elements remain.
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        # Push the new value onto the heap
        heapq.heappush(self.min_heap, val)
        
        # If the heap size exceeds k, remove the smallest element
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
            
        # The root of the min-heap is the kth largest element
        return self.min_heap[0]