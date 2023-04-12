# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def postorder(node,res):
            if not node:
                return None
            postorder(node.left,res)
            postorder(node.right,res)
            res.append(node.val)

        postorder(root,res)

        return res