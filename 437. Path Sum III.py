# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> int:
        global cnt
        cnt=0
        def func(root,dic,pref):
            global cnt
            if root:
                pref+=root.val
                rem=pref-target
                if rem in dic:
                    cnt+=dic[rem]
                if pref not in dic:
                    dic[pref]=1
                else:
                    dic[pref]+=1
                func(root.left,dic,pref)
                func(root.right,dic,pref)
                dic[pref]-=1
        func(root,{0:1},0)
        return cnt
''' Time Complexity--O(n)
    Space Complexity--O(h)'''
