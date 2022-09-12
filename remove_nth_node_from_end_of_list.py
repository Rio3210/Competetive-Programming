# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        if(head.next==None):
            return None
        count=1
        current=head
        while(current.next!=None):
            count+=1            
            current=current.next
        if(count==n):
            return head.next
        current=head 
        for i in range(count-n-1):
            current=current.next
        current.next=current.next.next
        return head
