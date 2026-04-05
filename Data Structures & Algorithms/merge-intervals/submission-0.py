from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 1. Edge case: If the list is empty, return early
        if not intervals:
            return []

        # 2. Sort the intervals based on their start times
        # This guarantees we process them in chronological order
        intervals.sort(key=lambda x: x[0])

        # 3. Initialize the result list with the first interval to act as our baseline
        result = [intervals[0]]

        # 4. Loop through the rest of the intervals
        for i in range(1, len(intervals)):
            current = intervals[i]
            last_added = result[-1]

            # Condition A: No overlap
            # If the current interval starts strictly after the last added one ends, 
            # they are completely separate. Add it to our results.
            if current[0] > last_added[1]:
                result.append(current)
            
            # Condition B: Overlap exists
            # Otherwise, they overlap. We update the end time of the last added interval
            # to be the maximum of both end times. (The start time is already correct due to sorting).
            else:
                last_added[1] = max(last_added[1], current[1])

        return result