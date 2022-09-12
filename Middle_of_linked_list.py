# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        
        list1=[]
        while head is not None:
            list1.append(head)
            head=head.next
        return list1[len(list1)//2]
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
