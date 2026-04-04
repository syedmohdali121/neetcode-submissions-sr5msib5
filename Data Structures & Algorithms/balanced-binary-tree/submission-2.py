# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.is_balanced = True
    
    def calc_bal(self, root):
        if root is None:
            return 0
        
        # FIX: Call the helper function recursively to get the actual depth
        left_depth = self.calc_bal(root.left)
        right_depth = self.calc_bal(root.right)

        # Update the global diameter tracker
        if abs(left_depth - right_depth) > 1:
            self.is_balanced = False
        
        # Return the depth of the current node to the parent
        return 1 + max(left_depth, right_depth)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.calc_bal(root)
        return self.is_balanced

        