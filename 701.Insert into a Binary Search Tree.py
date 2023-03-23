# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def func(root,val):
            x=root
            if root is None:
                return TreeNode(val)
            while root:
                if root.val>val and root.left is None:
                    root.left=TreeNode(val)
                    break
                elif root.val<val and root.right is None:
                    root.right=TreeNode(val)
                    break
                elif root.val>val:
                    root=root.left
                else:
                    root=root.right
            return x
        return func(root,val)
''' Time Complexity--O(logN)
    Space Complexity--O(1)'''
