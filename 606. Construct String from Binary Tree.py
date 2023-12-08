# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        global st
        st=''
        def preorder(root):
            global st
            st+=str(root.val)
            if root.left and root.right:
                st+='('
                preorder(root.left)
                st+=')'
                st+='('
                preorder(root.right)
                st+=')'
            elif root.left and not root.right:
                st+='('
                preorder(root.left)
                st+=')'
            elif not root.left and root.right:
                st+='()('
                preorder(root.right)
                st+=')'
        preorder(root)
        return st
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
