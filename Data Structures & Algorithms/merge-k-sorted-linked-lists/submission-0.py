# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        new_head = ListNode()
        curr = new_head

        nodes = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(nodes, (node.val, i, node))
        
        
        while nodes:
            val, i, node = heapq.heappop(nodes)
            curr.next = node
            curr = curr.next
            node = node.next
            if node:
                heapq.heappush(nodes, (node.val, i, node))
            
        return new_head.next
        


                