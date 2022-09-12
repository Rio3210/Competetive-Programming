# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        arr = []
        curr = head
        while curr!=None:
            arr.append(curr.val)
            curr = curr.next
        arr2 = []
        arr1 = []
        count = 0
        for i in range(len(arr)):
            if count%k !=0 and count!=0:
                arr1.append(arr[i])
                count+=1
            else:
                arr2.extend(arr1[::-1])
                arr1 = []
                arr1.append(arr[i])
                count = 1
        if len(arr1)%k == 0:
            arr2.extend(arr1[::-1])
        else:
            arr2.extend(arr1)  
        a = ListNode()
        dummy = a
        for i in range(len(arr2)):
            dummy.next = ListNode(arr2[i])
            dummy = dummy.next
        return a.next        
 
        
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
