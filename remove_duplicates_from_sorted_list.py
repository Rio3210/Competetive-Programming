# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    
    def deleteDuplicates(self, head):
                original = head 
                if original == None:
                        return head
                else:
                        while original.next != None:
                                if original.val == original.next.val:
                                        original.next = original.next.next
                                else:
                                        original= original.next
                return head

        
