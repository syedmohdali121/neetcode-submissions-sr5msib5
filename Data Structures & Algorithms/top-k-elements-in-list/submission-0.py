class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top_freq = {}
        for num in nums:
            top_freq[num] = top_freq.get(num, 0) + 1

        # Sort the keys based on their frequency (value in the dictionary)
        sorted_keys = sorted(top_freq.keys(), key=lambda x: top_freq[x], reverse=True)
        
        # Return the first k elements
        return sorted_keys[:k]
        

        