# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        
        curr = head
        max_val = 0
        arr = []
        while curr is not None:
            arr.append(curr.val)
            curr = curr.next 
        l, r = 0, len(arr) - 1
        while l < r:
            max_val = max( max_val, arr[l] + arr[r] )
            l += 1
            r -= 1
            
        return max_val
        
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        
