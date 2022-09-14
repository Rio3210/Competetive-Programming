# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#solution one easy and fast
class Solution(object):
    def sortList(self, head):
		if not head:
			return None
		myList=[]
		while head:
			myList.append(head.val)
			head=head.next
		myList.sort()
		newHead=point=ListNode(0)
		for i in range(len(myList)):
			point.next=ListNode(myList[i])
			point=point.next
		return newHead.next
        
#solution2
#Using merge sort
class Solution(object):
    def merge(self, l1, l2):
        res = None
        temp = None
        while l1 is not None and l2 is not None:
            if res is None:
                if l1.val < l2.val:
                    res = l1
                    l1=l1.next
                    temp = res
                else:
                    res = l2
                    l2=l2.next
                    temp = res
                temp.next = None
            else:
                if l1.val < l2.val:
                    temp.next = l1
                    l1=l1.next
                else:
                    temp.next = l2
                    l2=l2.next
                temp = temp.next
                temp.next = None
            
        if l1 is not None:
            temp.next = l1
        else:
            temp.next = l2
            
        return res
    
    def mergesort(self, head):
        if head and head.next:
            fast = head
            slow = head
            while fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            head2 = slow.next
            slow.next = None
            head = self.mergesort(head)
            head2 = self.mergesort(head2)
            return self.merge(head, head2)
        return head
    
    def sortList(self, head):
        return self.mergesort(head)
        
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
