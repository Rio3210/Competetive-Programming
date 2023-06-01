# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        ans=[]
        def helper(root):
            nonlocal ans
            if root == None:
                return
            helper(root.left)
            ans.append(root)
            helper(root.right)

        helper(root)
        # print(ans)
        sort=sorted(i.val for i in ans)
        for i in range(len(sort)):
            ans[i].val=sort[i]
            
            
            
        """
        Do not return anything, modify root in-place instead.
        """
        