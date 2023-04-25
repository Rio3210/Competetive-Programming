# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=[(root,0,0)]
        ans=defaultdict(list)
        while q:
            ln=len(q)
            
            for x in range(ln):
                node,r,c=q.pop()
                ans[c].append((r,node.val))
                if node.left:
                    q.append((node.left,r+1,c-1))
                if node.right:
                    q.append((node.right,r+1,c+1))     
        # print(ans)
        for i in ans:
            ans[i].sort()
            x=ans[i]
            for i,val in enumerate(x):
                x[i]=val[1]
        # print(ans)
        for i in ans:
            ans[i]
        result = []
        for val in sorted(ans.keys()):
            result.append(ans[val])
        return result
        
        
        