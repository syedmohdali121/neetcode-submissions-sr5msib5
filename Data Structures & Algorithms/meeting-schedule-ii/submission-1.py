import heapq
from typing import List

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        # 1. Sort the meetings by start time
        intervals.sort(key=lambda x: x.start)
        
        # 2. Initialize a min-heap to keep track of the end times of meetings 
        # currently occupying rooms.
        free_rooms = []
        
        # Add the first meeting's end time to the heap
        heapq.heappush(free_rooms, intervals[0].end)
        
        # 3. Iterate through the remaining meetings
        for i in range(1, len(intervals)):
            current_meeting = intervals[i]
            
            # If the room that frees up the earliest (free_rooms[0]) is empty 
            # by the time the current meeting starts, we can reuse it!
            if current_meeting.start >= free_rooms[0]:
                # Remove that room's old end time from the heap
                heapq.heappop(free_rooms)
                
            # Whether we reused a room or had to allocate a new one, 
            # the current meeting's end time needs to be added to the heap.
            heapq.heappush(free_rooms, current_meeting.end)
            
        # The size of the heap tells us how many rooms are currently active
        return len(free_rooms)