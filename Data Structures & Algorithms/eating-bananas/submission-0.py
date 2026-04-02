import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # The minimum possible eating speed is 1
        # The maximum possible eating speed is the size of the largest pile
        l = 1
        r = max(piles)
        
        # We want to keep track of the best (minimum) valid speed we've found
        optimal_speed = r 
        
        while l <= r:
            mid_speed = (l + r) // 2
            
            # Calculate total hours required at the current mid_speed
            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile / mid_speed)
            
            # If we can finish within h hours, this speed works.
            # But we want the MINIMUM speed, so let's try a slower speed (left half).
            if total_hours <= h:
                optimal_speed = mid_speed # Save this as a potential answer
                r = mid_speed - 1
            else:
                # We took too long! We must eat faster (right half).
                l = mid_speed + 1
                
        return optimal_speed