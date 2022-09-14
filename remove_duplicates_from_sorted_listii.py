# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        curr = head
        prev = ListNode(0)
        prev.next = curr
        rec = prev
        while curr:
            dupl = False 
            while curr.next and curr.val == curr.next.val:
                dupl = True
                curr = curr.next
            if dupl:
                curr = curr.next
                prev.next = curr
            else:
                prev = curr
                curr = curr.next
        return rec.next
        

        """
        :type head: ListNode
        :rtype: ListNode
        """
        
