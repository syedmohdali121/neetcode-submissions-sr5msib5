from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # This creates a dictionary where the default value is an empty list
        res = defaultdict(list)
        
        for s in strs:
            # Create a fresh 26-element array for the current string
            count = [0] * 26
            
            # Count the characters using our ord() trick
            for char in s:
                count[ord(char) - ord('a')] += 1
                
            # Convert the list to a tuple so it can be a dictionary key!
            # Then append the original string to that key's list.
            res[tuple(count)].append(s)
            
        # We only want the grouped lists, not the tuple keys
        return list(res.values())