# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        global prev
        prev=None
        def func(root):
            global prev
            if not root:
                return 
            func(root.right)
            func(root.left)
            root.right=prev
            root.left=None
            prev=root
        func(root)
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
