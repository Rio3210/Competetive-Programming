# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:  
        def in_order_traversal(node):
            if node is None:
                return []
            return (in_order_traversal(node.left) 
            + [node.val] + in_order_traversal(node.right))
        
        nodes = in_order_traversal(root)
        # print(nodes)
        for i in range(1, len(nodes)):
            if nodes[i-1] >= nodes[i]:
                return False
        return True
    
    
    
        # def helper(root,left,right):
        #     if not root:
        #         return True
        #     if not (root.val>left and root.val<right):
        #         return False
        #     return helper(root.left,left,root.val)and helper(root.right,root.val,right)
        # return helper(root,-inf,inf)