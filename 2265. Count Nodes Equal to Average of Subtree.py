# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        global totcnt
        totcnt=0
        def func(root):
            global totcnt
            if not root:
                return 0,0
            cnt1,tot1=func(root.left)
            cnt2,tot2=func(root.right)
            if (tot1+tot2+root.val)//(cnt1+cnt2+1)==root.val:
                totcnt+=1
            return cnt1+cnt2+1,tot1+tot2+root.val
        func(root)
        return totcnt
''' Time Complexity--O(n)
    Space Complexity--O(1)'''
