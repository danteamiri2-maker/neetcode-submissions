# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root:
                return [0, True]

            l_height, l_balanced = dfs(root.left)
            r_height, r_balanced = dfs(root.right)
            new_height = 1 + max(l_height, r_height)

            if abs(l_height - r_height) > 1:
                return [new_height, False]

            return [new_height, l_balanced and r_balanced]

        height, is_balanced = dfs(root)
        return is_balanced
            

            


        
        
        