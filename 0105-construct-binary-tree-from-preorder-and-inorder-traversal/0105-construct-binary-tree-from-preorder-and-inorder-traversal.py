# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def helper(pre,ino):
            if not ino:
                return None
            root_val=pre.pop(0)
            root=TreeNode(root_val)
            ind=ino.index(root_val)
            root.left=helper(pre,ino[:ind])
            root.right=helper(pre,ino[ind+1:])
            return root
        return helper(preorder,inorder)