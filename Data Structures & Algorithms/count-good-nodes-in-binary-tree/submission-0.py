# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        # Helper function that tracks the max value seen on the current path
        def dfs(node, max_so_far):
            # Base case: if we hit an empty node, it contributes 0 good nodes
            if not node:
                return 0
            
            # 1. Check if the current node is "good"
            # (If its value is greater than or equal to the max seen on this path)
            good_count = 1 if node.val >= max_so_far else 0
            
            # 2. Update the max value for the children to use
            new_max = max(max_so_far, node.val)
            
            # 3. Recursively ask the left and right children how many good nodes they have
            left_count = dfs(node.left, new_max)
            right_count = dfs(node.right, new_max)
            
            # 4. Bubble the total sum back up the tree
            return good_count + left_count + right_count
            
        # Kick off the DFS. 
        # The root is always a good node, so the initial max is just the root's value.
        return dfs(root, root.val)