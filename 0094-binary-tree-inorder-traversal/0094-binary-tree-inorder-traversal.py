# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack=[]
        if root is None:
            return []
        def helper(root):
            if root:
                left=helper(root.left)
                stack.append(root.val)
                right=helper(root.right)
            return stack
        return helper(root)
                