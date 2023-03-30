# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        stack=[]
        def helper(root):
            if not root:
                return 
            helper(root.left)
            stack.append(root.val)
            helper(root.right)
            return stack
        c=Counter(helper(root))
        maxxi=max(c.values())
        ans=[]
        for i in c:
            if c[i]==maxxi:
                ans.append(i)
        return ans
        # maxx=[-10^6]
        # c=Counter(helper(root))
        # print(c)
        # for i in c:
        #     if c[i]>c[maxx[-1]]:
        #         maxx[-1]=i
        #     elif c[i]==c[maxx[-1]]:
        #         maxx.append(i)
        # return maxx