class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        # nums_dedup = list(set(nums))
        # nums_sorted = sorted(nums_dedup)
        
        # longest = 1
        # current_streak = 1
        
        # # Start at index 1 and compare to index i-1
        # for i in range(1, len(nums_sorted)):
        #     if nums_sorted[i] == nums_sorted[i-1] + 1:
        #         # It's consecutive! Grow the streak.
        #         current_streak += 1
        #     else:
        #         # The streak broke. Reset back to 1.
        #         current_streak = 1
                
        #     # Keep track of the highest streak we've seen so far
        #     longest = max(longest, current_streak)
            
        # return longest
        
        num_set = set(nums)
        longest = 0
        
        # Iterate over the set directly (avoids duplicate starting points)
        for num in num_set:
            # Check if it's the START of a sequence
            if (num - 1) not in num_set:
                current_num = num
                current_streak = 1
                
                # Now we count upwards as far as we can go
                while (current_num + 1) in num_set:
                    current_num += 1
                    current_streak += 1
                    
                longest = max(longest, current_streak)
                
        return longest