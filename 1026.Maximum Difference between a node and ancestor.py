# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.result=0
        def helper(curr,curr_min,curr_max):
            if not curr:
                return 
            self.result=max(self.result,abs(curr_max-curr.val),abs(curr_min-curr.val))
            curr_min=min(curr_min,curr.val)
            curr_max=max(curr_max,curr.val)
            helper(curr.left,curr_min,curr_max)
            helper(curr.right,curr_min,curr_max)
        helper(root,root.val,root.val)
        return self.result
