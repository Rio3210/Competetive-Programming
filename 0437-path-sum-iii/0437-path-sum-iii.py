# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count=0
        def helper(root,target):
            nonlocal count
            if not root:
                return 
            if target==root.val:
                count+=1
            helper(root.left,target-root.val)
            helper(root.right,target-root.val)
        def dfs(root,target):
            if not root:
                return 
            helper(root,target)
            dfs(root.left,target)
            dfs(root.right,target)
        dfs(root,targetSum)
        return count