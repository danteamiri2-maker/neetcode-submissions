# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def reverse(curr):
            if not curr:
                pass

            else:
                if curr.left and curr.right:
                    tmp = curr.left
                    curr.left = curr.right
                    curr.right = tmp

                    reverse(curr.left)
                    reverse(curr.right)

                elif curr.left:
                    tmp = curr.left
                    curr.left = curr.right
                    curr.right = tmp
                    reverse(curr.right)

                elif curr.right:
                    tmp = curr.right
                    curr.right = curr.left
                    curr.left = tmp
                    reverse(curr.left)
            
        

        reverse(root)
        return root
            
        

            