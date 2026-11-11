# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def recurse(curr, depth):
            if not curr:
                return depth

            elif not curr.left and not curr.right:
                return depth + 1

            else:
                l = 0
                r = 0
                if curr.left:
                    l = recurse(curr.left, depth + 1)
                
                if curr.right:
                    r = recurse(curr.right, depth + 1)

                return max(l, r)

         
        return recurse(root, 0)
