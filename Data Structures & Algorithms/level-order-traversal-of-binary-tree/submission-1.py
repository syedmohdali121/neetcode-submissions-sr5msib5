# 1. Import deque from the collections module
from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
    
        result = []
        # 2. Wrap your initial list with deque()
        queue = deque([root])  
        
        while queue:
            level = []
            for _ in range(len(queue)):
                # 3. Use popleft() instead of pop(0)
                node = queue.popleft() 
                
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        
        return result