# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p==None and q!=None:
            return False
        elif p!=None and q==None:
            return False
        elif p==None and q==None:
            return True
        
        if p.val == q.val:
            left_is_same = self.isSameTree(p.left, q.left)
            right_is_same = self.isSameTree(p.right, q.right)
            return left_is_same and right_is_same
        else:
            return False

        
        
        