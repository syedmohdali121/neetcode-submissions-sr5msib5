class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root
        
        while curr:
            # If both p and q are greater than curr, go right
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            
            # If both p and q are less than curr, go left
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            
            # We found the split point! (Or one of them equals curr)
            else:
                return curr