class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # s_sorted = sorted(s)
        # t_sorted = sorted(t)
        
        # for i in range(0, len(s_sorted)):
        #     if(s_sorted[i] != t_sorted[i]):
        #         return False
        
        # return True
        countS, countT = {}, {}
        
        # Build the frequency maps
        for i in range(len(s)):
            # .get() safely returns 0 if the character isn't in the dict yet
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1
            
        # Compare the two frequency maps
        for char in countS:
            if countS[char] != countT.get(char, 0):
                return False
                
        return True

        