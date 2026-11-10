# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        

        s = 0
        carry = 0
        k = 0
        res = []
        while l1 or l2: # stops too early, need something else

            if l1 and l2:
                d1, d2 = l1, l2
                l1 = l1.next
                l2 = l2.next
                tmp = carry + d1.val + d2.val


            elif l1:
                d1 = l1
                l1 = l1.next
                tmp = carry + d1.val


            elif l2:
                d2 = l2
                l2 = l2.next
                tmp = carry + d2.val

            if tmp > 9:
                carry = tmp // 10
                tmp = tmp % 10
            else:
                carry = 0
            
            res.append(tmp)

        
        if carry > 0:
            res.append(carry)
            carry = 0

 
        print(res)

        dummy = ListNode()
        while res:
            d = res.pop()
            if dummy.next:
                tmp = dummy.next
                dummy.next = ListNode(d, tmp)
            else:
                dummy.next = ListNode(d, None)
        
        return dummy.next
        
