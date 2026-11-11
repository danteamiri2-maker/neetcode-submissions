# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        


        def getAncestor(root, small, large):
            if small.val <= root.val and large.val >= root.val:
                return root 
            elif large.val <= root.val:
                return getAncestor(root.left, small, large)
            elif small.val >= root.val:
                return getAncestor(root.right, small, large)
            return root


        smaller = p if p.val < q.val else q
        larger = q if p.val < q.val else p

        return getAncestor(root, smaller, larger)

