# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def helper(root):
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            rightchild=root.right
            lastRight=findLastRight(root.left)
            lastRight.right=rightchild
            return root.left
        def findLastRight(root):
            if root.right is None:
                return root
            return findLastRight(root.right)
        if root is None:
            return None
        if root.val==key:
            return helper(root)
        dummy=root
        while root:
            if root.val>key:
                if root.left  and root.left.val==key:
                    root.left=helper(root.left)
                    break
                else:
                    root=root.left
            else:
                if root.right and root.right.val==key:
                    root.right=helper(root.right)
                    break
                else:
                    root=root.right
        return dummy

''' Time Complexity--O(height of the tree)
    Space Complexity--O(1)'''
