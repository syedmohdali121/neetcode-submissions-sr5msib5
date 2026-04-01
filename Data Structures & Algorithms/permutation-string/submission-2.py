class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # If s1 is longer than s2, it can't possibly be a substring
        if len(s1) > len(s2):
            return False
            
        # Create arrays of size 26 to store character frequencies
        s1_counts = [0] * 26
        window_counts = [0] * 26
        
        # 1. Initialize the first window
        for i in range(len(s1)):
            s1_counts[ord(s1[i]) - ord('a')] += 1
            window_counts[ord(s2[i]) - ord('a')] += 1
            
        # Check if the very first window is a match
        if s1_counts == window_counts:
            return True
            
        # 2. Slide the window across the rest of s2
        l = 0
        for r in range(len(s1), len(s2)):
            # Add the new character on the right
            window_counts[ord(s2[r]) - ord('a')] += 1
            
            # Remove the old character on the left
            window_counts[ord(s2[l]) - ord('a')] -= 1
            l += 1
            
            # 3. Compare the arrays
            if s1_counts == window_counts:
                return True
                
        return False