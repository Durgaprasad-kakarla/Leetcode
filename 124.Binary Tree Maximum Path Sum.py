# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res=[root.val]
        def dfs(root):
            if not root:
                return 0
            leftmax=dfs(root.left)#find the maximum sum of left subtree
            rightmax=dfs(root.right)#finding the maximum sum of right subtree
            leftmax=max(leftmax,0)#make sure that the left max is greater than 0
            rightmax=max(rightmax,0)#make sure that the right max is greater than 0
            res[0]=max(res[0],root.val+leftmax+rightmax)#store the max value if it is greater than the value in res[0],root.val,leftmax and rightmax
            return root.val+max(leftmax,rightmax)#return maximum path sum
        dfs(root)
        return res[0]
