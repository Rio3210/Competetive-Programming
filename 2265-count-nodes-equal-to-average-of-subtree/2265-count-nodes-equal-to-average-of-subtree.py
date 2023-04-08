# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        count=0
        def helper(root):
            nonlocal count
            if not root:
                return 0,0
            lsum,lcnt=helper(root.left)
            rsum,rcnt=helper(root.right)
            currsum=lsum+rsum+root.val
            temp_count=lcnt+rcnt+1
            if temp_count!=0 and root.val==currsum//temp_count:
                count+=1
            return currsum,temp_count
        helper(root)
        return count
            