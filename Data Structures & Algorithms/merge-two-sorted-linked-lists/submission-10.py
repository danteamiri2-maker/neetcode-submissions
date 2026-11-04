# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1 and not list2:
            return list1
        
        
        dummy = node = ListNode()
        curr1, curr2 = list1, list2
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                node.next = curr1
                node = node.next
                curr1 = curr1.next
            elif curr1.val > curr2.val:
                node.next = curr2
                node = node.next
                curr2 = curr2.next
        
        while curr1:
            node.next = curr1
            node = node.next
            curr1 = curr1.next
        
        while curr2:
            node.next = curr2
            node = node.next
            curr2 = curr2.next

        return dummy.next