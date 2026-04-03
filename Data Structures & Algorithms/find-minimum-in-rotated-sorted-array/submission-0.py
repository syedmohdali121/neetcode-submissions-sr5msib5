from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        
        while l < r:
            mid = (l + r) // 2
            
            # Compare middle element with the rightmost element
            if nums[mid] > nums[r]:
                # The drop (minimum element) is to the right
                l = mid + 1
            else:
                # The right side is sorted, minimum is mid or to the left
                r = mid
                
        # When l == r, we have found the minimum element
        return nums[l]