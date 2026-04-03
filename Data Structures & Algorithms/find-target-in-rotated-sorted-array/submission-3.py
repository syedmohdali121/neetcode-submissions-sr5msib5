class Solution:
    def binary_search(self, l, r, nums, target):
        if l > r:
            return -1
        
        mid = (l+r)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.binary_search(l, mid-1, nums, target)
        else:
            return self.binary_search(mid+1, r, nums, target)

    def search(self, nums: List[int], target: int) -> int:
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
        deflection_point =  l
        res = False
        res = self.binary_search(0, deflection_point-1, nums, target)
        if res!= -1:
            return res
        
        res = self.binary_search(deflection_point, len(nums)-1, nums, target)

        return res
        
        
        