# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isvalid(root,min1,max1):
            if root is None:
                return True
            if root.val>=max1 or root.val<=min1:
                return False
            return  isvalid(root.left,min1,root.val) and isvalid(root.right,root.val,max1)
        return isvalid(root,sys.maxsize*(-1),sys.maxsize)
 '''Time Complexity--O(n)
    Space Complexity--O(1)'''
