# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def height(root):
            if root is None:#if root is Null then its height is zero
                return 0
            else:
                return max(height(root.left),height(root.right))+1#here we can find the height of the binary tree in both sides from root
        return height(root)
"Time Complexity:O(n)--------Space Complexity:O(h) here h is is height of binary tree and n is no of nodes in the tree'''
