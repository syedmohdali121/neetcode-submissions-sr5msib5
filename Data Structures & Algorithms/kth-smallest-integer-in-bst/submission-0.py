class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # A list to store our sorted values
        sorted_values = []
        
        # Helper function for recursive in-order traversal
        def inorder(node):
            if node is None:
                return
            
            inorder(node.left)           # 1. Go Left
            sorted_values.append(node.val) # 2. Process Current
            inorder(node.right)          # 3. Go Right
            
        inorder(root)
        
        # Return the k-th element (0-indexed, so we use k-1)
        return sorted_values[k - 1]