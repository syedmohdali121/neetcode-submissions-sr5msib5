# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def __init__(self):
        self.max_d = 0

    def calculateD(self, root, d):
        if root is None:
            return

        d+=1
        self.max_d = max(self.max_d, d)
        
        self.calculateD(root.left, d)
        self.calculateD(root.right, d)


    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.calculateD(root, 0)

        return self.max_d
        