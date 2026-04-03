from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is always the smaller array to optimize the search space
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        left = 0
        right = m
        
        # Calculate the required size of the left partition across both arrays combined
        half_len = (m + n + 1) // 2
        
        while left <= right:
            # i is the partition index for nums1
            i = (left + right) // 2
            # j is the corresponding partition index for nums2
            j = half_len - i
            
            # Extract the 4 values directly around the partition lines.
            # If a partition is at the extreme edge, use infinity to bypass the check.
            left1 = nums1[i - 1] if i > 0 else float('-inf')
            right1 = nums1[i] if i < m else float('inf')
            
            left2 = nums2[j - 1] if j > 0 else float('-inf')
            right2 = nums2[j] if j < n else float('inf')
            
            # Check if we have found a valid partition
            if left1 <= right2 and left2 <= right1:
                # If the total number of elements is odd, the median is the largest 
                # element on the left side of the partition.
                if (m + n) % 2 == 1:
                    return float(max(left1, left2))
                
                # If the total number of elements is even, the median is the average 
                # of the largest on the left and the smallest on the right.
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2.0
                    
            # If the left side of nums1 is too big, the partition in nums1 needs to move left.
            elif left1 > right2:
                right = i - 1
                
            # Otherwise, the partition in nums1 needs to move right.
            else:
                left = i + 1

        # The problem guarantees a valid median will be found, so this won't be reached
        return 0.0