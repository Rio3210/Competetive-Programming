# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self,root):
        paths = []
        def helper(root, path, paths):    
            if root.left is None and root.right is None:
                paths.append(path + str(root.val))
                # print(paths)
            if root.left is not None:
                helper(root.left, path + str(root.val) + "->", paths)
            if root.right is not None: 
                helper(root.right, path + str(root.val) + "->", paths)
        if root is not None:
            helper(root, "", paths)
        return paths

    
            