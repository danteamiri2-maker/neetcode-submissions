# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def areEqual(node1, node2):
            if not node1 and not node2:
                return True
            
            if not node1 and node2:
                return False
            
            if node1 and not node2:
                return False

            if node1.val == node2.val:
                right = areEqual(node1.right, node2.right)
                left = areEqual(node1.left, node2.left)
                return right and left
            
            else:
                return False
            
        roots = []
        def collectRoots(root):
            if not root:
                pass
            elif root:
                roots.append(root)
                if root.left:
                    collectRoots(root.left)
                if root.right:
                    collectRoots(root.right)
        
        collectRoots(root)
        contains_subroot = False
        while roots and not contains_subroot:
            curr = roots.pop()
            contains_subroot = areEqual(curr, subRoot)

        return contains_subroot
        

                

