# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        global mini
        mini=''
        def inorder(root,s):
            global mini
            if root:
                if not root.left and not root.right:
                    s=chr(root.val+97)+s
                    if mini=='':
                        mini=s
                    if mini>s:
                        mini=s
                inorder(root.left,chr(root.val+97)+s)
                inorder(root.right,chr(root.val+97)+s)
        inorder(root,'')
        return mini
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
