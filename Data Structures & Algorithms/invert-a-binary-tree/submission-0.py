class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case: if the tree is empty, return None
        if root is None:
            return None

        # 1. Swap the left and right children unconditionally
        # (Python allows you to swap variables in one line without a temp variable!)
        root.left, root.right = root.right, root.left
        
        # 2. Recursively invert the left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        # 3. Return the root node so the caller gets the modified tree
        return root