# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
            
        stack = [(root, None, None)]
        ans = 0
        while stack:
            node, parent, grandp = stack.pop()
            if grandp and grandp.val % 2 == 0:
                ans += node.val
            if node.left:
                stack.append((node.left, node, parent))
            if node.right:
                stack.append((node.right, node, parent))
        return ans
        
            
            