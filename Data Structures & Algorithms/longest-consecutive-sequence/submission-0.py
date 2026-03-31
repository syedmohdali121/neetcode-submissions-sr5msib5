class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        nums_dedup = list(set(nums))
        nums_sorted = sorted(nums_dedup)
        
        longest = 1
        current_streak = 1
        
        # Start at index 1 and compare to index i-1
        for i in range(1, len(nums_sorted)):
            if nums_sorted[i] == nums_sorted[i-1] + 1:
                # It's consecutive! Grow the streak.
                current_streak += 1
            else:
                # The streak broke. Reset back to 1.
                current_streak = 1
                
            # Keep track of the highest streak we've seen so far
            longest = max(longest, current_streak)
            
        return longest