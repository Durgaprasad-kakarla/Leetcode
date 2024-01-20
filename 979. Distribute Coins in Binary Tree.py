# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        global ans
        ans=0
        def func(node):
            global ans
            if not node:
                return 0
            left,right=func(node.left),func(node.right)
            ans+=abs(left)+abs(right)
            return node.val+left+right-1
        func(root)
        return ans
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
