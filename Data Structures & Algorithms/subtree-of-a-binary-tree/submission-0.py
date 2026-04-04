# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # 1. Paste your exact Same Tree logic here as a helper
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    # 2. Your main function
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Base Case 1: If subRoot is empty, it's technically always a subtree
        if not subRoot:
            return True
            
        # Base Case 2: If we reach the end of the big tree without finding a match
        if not root:
            return False
            
        # Check if the trees match starting at the CURRENT node
        if self.isSameTree(root, subRoot):
            return True
            
        # If they don't match, keep searching down the left OR the right side of the big tree
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)