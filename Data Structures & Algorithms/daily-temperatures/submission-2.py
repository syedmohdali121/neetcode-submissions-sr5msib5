class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        out = [0] * len(temperatures)
        stack = []  # Stores indices, not temperatures

        for current_day, current_temp in enumerate(temperatures):
            # While the stack has items AND today's temp is warmer than the 
            # temperature of the day currently at the top of the stack
            while stack and current_temp > temperatures[stack[-1]]:
                # We found a warmer day for 'prev_day'!
                prev_day = stack.pop()
                
                # Calculate how many days we waited
                out[prev_day] = current_day - prev_day
            
            # Add today to the stack to wait for a warmer day
            stack.append(current_day)
            
        return out