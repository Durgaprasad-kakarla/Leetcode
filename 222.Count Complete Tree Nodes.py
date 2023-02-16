# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def getsize(root):
            if root is None:
                return 0
            else:
                return 1+getsize(root.left)+getsize(root.right)
        return getsize(root)
'''Time Complexity:O(n)  Space Complexity:O(h)'''
