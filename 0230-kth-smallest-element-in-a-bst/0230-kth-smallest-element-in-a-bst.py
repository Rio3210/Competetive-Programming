# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def helper(root): 
            if not root:
                return [] 
            return (helper(root.left) 
            + [root.val] + helper(root.right))
        return helper(root)[k-1]