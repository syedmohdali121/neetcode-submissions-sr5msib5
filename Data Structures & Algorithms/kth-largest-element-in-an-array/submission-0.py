import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if nums is None:
            return None

        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        while k!=1:
            heapq.heappop(max_heap)
            k-=1

        return -(heapq.heappop(max_heap))

        
        