class Solution:
    def binary_search(self, l, r, nums, target):
        if l >= r:
            return False
        
        mid = (l+r)//2
        if nums[mid] == target:
            return True
        elif nums[mid] > target:
            return self.binary_search(l, mid, nums, target)
        else:
            return self.binary_search(mid+1, r, nums, target)

    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        found = False
        for i in range(len(matrix)):
            l=0
            r = len(matrix[i])
            found = self.binary_search(l, r, matrix[i], target)
            if found:
                return True
            
        return False
        