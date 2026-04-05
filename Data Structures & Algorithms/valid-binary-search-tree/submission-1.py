class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # Helper function that takes the node and its allowed boundaries
        def validate(node, low=-float('inf'), high=float('inf')):
            # Base case: An empty node is always valid
            if node is None:
                return True
            
            # If the current node violates its boundaries, it's not a BST
            if node.val <= low or node.val >= high:
                return False
            
            # Recursively check the left and right subtrees with updated boundaries.
            # - Going left: The current node's value becomes the new 'high' ceiling.
            # - Going right: The current node's value becomes the new 'low' floor.
            left_is_valid = validate(node.left, low, node.val)
            right_is_valid = validate(node.right, node.val, high)
            
            return left_is_valid and right_is_valid
        
        # Kick off the recursion with the root and infinite boundaries
        return validate(root)