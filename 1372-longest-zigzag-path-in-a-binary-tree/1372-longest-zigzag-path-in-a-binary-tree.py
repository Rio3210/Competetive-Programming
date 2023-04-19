# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = 0
        stack = [(root, "left", 0), (root, "right", 0)] 
        while stack:
            node, direction, count = stack.pop()
            res = max(res, count)
            if direction == "left":
                if node.left:
                    stack.append((node.left, "right", count + 1))
                if node.right:
                    stack.append((node.right, "left", 1))
            else:
                if node.right:
                    stack.append((node.right, "left", count + 1))
                if node.left:
                    stack.append((node.left, "right", 1))
        return res