# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return ans
            curr = stack.pop()
            ans.append(curr.val)
            root = curr.right
            
          # stack
#         if root is None:
#             return []
#         def helper(root):
#             if root:
#                 helper(root.left)
#                 stack.append(root.val)
#                 helper(root.right)
#             return stack
#         return helper(root)
        