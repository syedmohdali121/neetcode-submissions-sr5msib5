class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j:
                    prod[i] = prod[i] * nums[j]
        
        return prod