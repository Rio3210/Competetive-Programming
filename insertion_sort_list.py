# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        result = []
        pointer = head
        while pointer:
            result.append(pointer.val)
            pointer = pointer.next
        
        result.sort()
        
        pointer = head
        i = 0
        while pointer:
            pointer.val = result[i]
            i+= 1
            pointer = pointer.next
        
        return head
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
