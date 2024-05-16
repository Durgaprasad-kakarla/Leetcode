# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def inorder(root):
            if not root.left and not root.right:
                if root.val==1:
                    return True
                return False
            left=inorder(root.left)
            right=inorder(root.right)
            if root.val==2:
                return left or right
            return left and right
        return inorder (root)
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
