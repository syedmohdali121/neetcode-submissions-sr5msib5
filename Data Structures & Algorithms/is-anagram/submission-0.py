class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_sorted = sorted(s)
        t_sorted = sorted(t)
        if len(s) != len(t):
            return False
        
        for i in range(0, len(s_sorted)):
            if(s_sorted[i] != t_sorted[i]):
                return False
        
        return True

        