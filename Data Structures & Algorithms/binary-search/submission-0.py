class Solution:
    def binary_search(self, l, r, nums, target):
        if l >= r:
            return -1
        
        mid = (l+r)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.binary_search(l, mid, nums, target)
        else:
            return self.binary_search(mid+1, r, nums, target)

    def search(self, nums: List[int], target: int) -> int:
        
        
        l = 0
        r = len(nums)

        num_index = self.binary_search(l, r, nums, target)
        return num_index
        