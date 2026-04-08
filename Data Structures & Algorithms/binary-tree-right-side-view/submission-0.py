from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            # Take a snapshot of how many nodes are in the current level
            level_length = len(queue)
            
            for i in range(level_length):
                node = queue.popleft()
                
                # THE MAGIC TRICK:
                # If this is the very last iteration of the loop for this level,
                # it means this is the rightmost node. Add it to our result.
                if i == level_length - 1:
                    result.append(node.val)
                
                # Queue up the children for the next level just like normal
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
        return result