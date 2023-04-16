# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        st=[]
        curr=head
        while curr:
            st.append(curr.val)
            curr=curr.next
        # print(st)
        def helper(nums,left,right):
            if left>right:
                return None
            mid=(left+right)//2
            root=TreeNode(nums[mid])
            root.left=helper(nums,left,mid-1)
            root.right=helper(nums,mid+1,right)
            return root
        return None if len(st)==0 else helper(st,0,len(st)-1)
            