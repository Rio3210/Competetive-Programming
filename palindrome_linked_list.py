# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        list1=[]
        while head is not None:
            list1.append(head.val)
            head=head.next
       
        if list1==list1[::-1]:
            return True
        return False
      
        
        """
        :type head: ListNode
        :rtype: bool
        """
        
