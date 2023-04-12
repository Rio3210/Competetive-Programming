# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        stack=[]
        def inorderTraverse(root):
            if not root:
                return 
            inorderTraverse(root.left)
            stack.append(root.val)
            inorderTraverse(root.right)
            
        def helper(nums,left,right): #helps to build a tree from a sorted array
            if left>right:
                return None
            mid=(left+right)//2
            root=TreeNode(nums[mid])
            root.left=helper(nums,left,mid-1)
            root.right=helper(nums,mid+1,right)
            return root
        inorderTraverse(root)
        return None if len(stack)==0 else helper(stack,0,len(stack)-1)
        