# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        lst=[]
        def inorder(root):
            if root:
                inorder(root.left)
                lst.append(root.val)
                inorder(root.right)
        inorder(root)
        def balance(lst):
            if not lst:
                return None
            mid=len(lst)//2
            root=TreeNode(lst[mid])
            root.left=balance(lst[:mid])
            root.right=balance(lst[mid+1:])
            return root
        return balance(lst)
''' Time Complexity--O(n)  
    Space Complexity--O(n)'''
