# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        stack=[(root,root.val)]
        
        while stack:
            root,currsum=stack.pop()
            
            if not root.right and not  root.left and currsum==targetSum:
                return True
            if root.left:
                stack.append((root.left,currsum+root.left.val))
            if root.right:
                stack.append((root.right,currsum+root.right.val))
        return False
#         def helper(root,currsum):
#             if not root:
#                 return False
#             if not root.left and not root.right:
#                 return currsum==targetSum
            
#             return helper(root.left,currsum+root.left.val)or helper(root.right,currsum+root.right.val)
            
#         return helper(root,0)
          
        