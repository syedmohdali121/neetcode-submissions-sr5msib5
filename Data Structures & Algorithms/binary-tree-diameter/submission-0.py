class Solution:
    def __init__(self):
        self.diameter = 0
    
    def calc_dia(self, root):
        if root is None:
            return 0
        
        # FIX: Call the helper function recursively to get the actual depth
        left_depth = self.calc_dia(root.left)
        right_depth = self.calc_dia(root.right)

        # Update the global diameter tracker
        self.diameter = max(self.diameter, left_depth + right_depth)
        
        # Return the depth of the current node to the parent
        return 1 + max(left_depth, right_depth)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.calc_dia(root)
        return self.diameter