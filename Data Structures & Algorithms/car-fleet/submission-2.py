class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # Pair each car's position and speed, and sort them descending by position
        # so we process the car closest to the target first.
        cars = sorted(zip(position, speed), reverse=True)
        
        fleets = 0
        time_to_beat = 0.0 # Time of the slowest fleet ahead of us
        
        for pos, spd in cars:
            # Calculate exact time to reach target
            time = (target - pos) / spd
            
            # If this car takes strictly longer than the fleet ahead of it,
            # it cannot catch up. It forms a new fleet.
            if time > time_to_beat:
                fleets += 1
                # This new fleet becomes the new bottleneck for cars behind it
                time_to_beat = time 
                
        return fleets