# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        pointer1 = list1
        pointer2 = list2
        dummy = node = ListNode()
        while pointer1 and pointer2:
            if pointer1.val < pointer2.val:
                node.next = pointer1
                pointer1 = pointer1.next
                node = node.next
                
            elif pointer1.val >= pointer2.val:
                node.next = pointer2
                pointer2 = pointer2.next
                node = node.next

        while pointer1:
            node.next = pointer1
            pointer1 = pointer1.next
            node = node.next

        while pointer2:
            node.next = pointer2
            pointer2 = pointer2.next
            node = node.next

        
        return dummy.next



            