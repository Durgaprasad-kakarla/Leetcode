# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def rangesum(node):
            nonlocal ans
            if node:
                if node.val>=low and node.val<=high:#if the node's value is in between low and high then add it to the ans
                    ans+=node.val
                if node.val>low:#if the node.val is greater than the low then go to the left subtree
                    rangesum(node.left)
                if node.val<high:#If the node.val is less than high then go to the right subtree
                    rangesum(node.right)
        ans=0
        rangesum(root)
        return ans
