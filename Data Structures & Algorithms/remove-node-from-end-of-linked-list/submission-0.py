# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        #find length of list
        l = 0
        curr = head
        while curr:
            curr = curr.next
            l += 1

        #if length equal to n
        if l == n:
            return head.next
        
        
        #find node before the element to be removed
        k = 0
        curr = head
        while k != l - n - 1:
            curr = curr.next
            k += 1
        
        curr.next = curr.next.next
        return head