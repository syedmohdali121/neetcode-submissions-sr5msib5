from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        n = len(intervals)
        
        # Phase 1: Add all intervals that come before the newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
            
        # Phase 2: Merge overlapping intervals
        # An overlap exists if the current interval's start <= newInterval's end
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        
        # Add the merged interval
        result.append(newInterval)
        
        # Phase 3: Add the rest of the intervals
        while i < n:
            result.append(intervals[i])
            i += 1
            
        return result