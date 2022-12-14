# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        if not head:
            return None
        prev = None
        
        while head:
            next = head.next
            head.next = prev

            prev = head
            head = next 
        return prev
        
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
