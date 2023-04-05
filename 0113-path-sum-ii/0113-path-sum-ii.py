# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        paths = []
        path=[]
        def helper(root, path, paths):    
            if root.left is None and root.right is None:
                # print(path)
                if sum(path+[root.val])==targetSum: 
                    # print(path)
                    paths.append(path+[root.val])
                    path=[]
                # print(paths)
            if root.left is not None:
                helper(root.left, path+[root.val], paths)
            if root.right is not None: 
                helper(root.right, path+[root.val], paths)
        if root is not None:
            helper(root, path, paths)
        return paths