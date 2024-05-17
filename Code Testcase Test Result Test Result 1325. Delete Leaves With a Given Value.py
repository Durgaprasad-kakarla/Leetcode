# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def delete(root,target):
            if root:
                delete(root.left,target)
                delete(root.right,target)
                if root.left:
                    if root.left.left is None and root.left.right is None and root.left.val==target:
                        root.left=None
                if root.right:
                    if root.right.left is None and root.right.right is None and root.right.val==target:
                        root.right=None
        delete(root,target)
        if not root.left and not root.right and root.val==target:
            return None
        return root
''' Time Complexity--O(n)
    Space Complexity--O(n)''''
