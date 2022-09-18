# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        dummy = cur = ListNode()
        nodes = []
        for i in lists:
            while i:
                nodes.append(i.val)
                i = i.next
        for x in sorted(nodes):
            cur.next = ListNode(x)
            cur = cur.next
        return dummy.next
            
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
