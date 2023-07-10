# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def func(root):
            if not root:
                return 0
            if root.left is None or root.right is None:
                return max(func(root.left),func(root.right))+1
            else:
                return min(func(root.left),func(root.right))+1
        return func(root)
''' Time Complexity--O(n)
    Space Complexity--O(n)--Auxilary Space'''
