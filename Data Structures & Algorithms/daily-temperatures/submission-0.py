class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = [0]*len(temperatures)

        for i in range(len(temperatures)-1):
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    out[i]= j-i
                    break
        
        return out