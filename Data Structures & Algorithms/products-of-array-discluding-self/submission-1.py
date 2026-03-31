class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_prod = [1] * n
        right_prod = [1] * n
        prod = [1] * n

        # 1. Build left products
        for i in range(1, n):
            left_prod[i] = left_prod[i-1] * nums[i-1]

        # 2. Build right products (looping backwards)
        for i in range(n - 2, -1, -1):
            right_prod[i] = right_prod[i+1] * nums[i+1]

        # 3. Multiply them together
        for i in range(n):
            prod[i] = left_prod[i] * right_prod[i]
        
        return prod