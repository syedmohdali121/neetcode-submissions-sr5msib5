class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()
        for ele in nums:
            if ele in nums_set:
                return True
            else:
                nums_set.add(ele)
        
        return False
        