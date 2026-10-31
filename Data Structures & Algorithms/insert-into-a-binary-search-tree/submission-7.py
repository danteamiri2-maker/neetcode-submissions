# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if root:

            parent = root
            curr = root
            while curr:
                parent = curr
                if curr.val > val:
                    #move curr to the left
                    curr = curr.left
                elif curr.val < val:
                    #move curr to the right
                    curr = curr.right

            if curr:
                # insert node
                if curr.val < val:
                    curr.right = TreeNode(val, None, None)
                elif curr.val > val:
                    curr.left = TreeNode(val, None, None)
            else:
                # insert node
                if parent.val < val:
                    parent.right = TreeNode(val, None, None)
                elif parent.val > val:
                    parent.left = TreeNode(val, None, None)

        
        else:
            root = TreeNode(val, None, None)

        return root
