# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def recurse(curr):
            if not curr:
                return 0

            return 1 + max(recurse(curr.left), recurse(curr.right))

            
        if not root:
            return 0
            
        l = recurse(root.left)
        r = recurse(root.right)
        diameter = l + r

        sub = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))


        return max(diameter, sub)










