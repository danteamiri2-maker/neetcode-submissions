# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle of the list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        

        # reverse second half
        second = slow.next #ensures that the 2nd half is shorter 
        prev = slow.next = None # slow.next=None ends the first list 
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        # merge lists
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2




            


            
