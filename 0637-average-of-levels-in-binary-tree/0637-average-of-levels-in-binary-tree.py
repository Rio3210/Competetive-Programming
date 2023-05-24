# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        queue=deque([root])
        ans=[]
        while queue:
            lenn=len(queue)
            store=[]
            for i in range(lenn):
                node=queue.popleft()
                store.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(store)
        av=[]
        for i in ans:
            av.append(sum(i)/len(i))
        return av