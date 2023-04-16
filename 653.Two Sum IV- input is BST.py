# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        list1=[]
        def inorder(root,list1):
            if root:
                inorder(root.left,list1)
                list1.append(root.val)
                inorder(root.right,list1)
        inorder(root,list1)
        l=0
        r=len(list1)-1
        while l<r:
            if list1[l]+list1[r]==k:
                return True
            elif list1[l]+list1[r]>k:
                r=r-1
            else:
                l=l+1
        return False
''' Time Complexity--O(N)
    Space Complexity--O(N)'''
