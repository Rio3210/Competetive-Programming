# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        p = None
        while head:
            q = head.next
            head.next = p
            p = head
            head = q
        return p

    def reorderList(self, head):
        if not head or not head.next:
            return 
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head1 = self.reverseList(slow.next)
        slow.next = None
        p = head
        q = head1
        while q:
            p_nxt = p.next
            q_nxt = q.next
            p.next = q
            q.next = p_nxt
            p = p_nxt
            q = q_nxt
        
        
        
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        
