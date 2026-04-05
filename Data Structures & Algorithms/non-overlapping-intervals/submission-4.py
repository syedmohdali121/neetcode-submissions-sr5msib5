from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0  # Should return 0 count, not an empty list

        # Sort by start time
        intervals.sort(key=lambda x: x[0])

        count_overlap = 0
        # Instead of keeping a whole result array, we only need to track the end time 
        # of the last valid interval we decided to keep.
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            current_start, current_end = intervals[i]

            # Condition A: No overlap
            if current_start >= prev_end:
                # We keep this interval, so it becomes our new baseline end
                prev_end = current_end
            
            # Condition B: Overlap exists
            else:
                count_overlap += 1
                # We must remove one. To leave the most room for future intervals, 
                # we conceptually "keep" the one that ends earlier.
                prev_end = min(prev_end, current_end)

        return count_overlap