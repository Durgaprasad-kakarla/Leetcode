# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        global tot
        tot=0
        def func(root,dic):
            global tot
            if root:
                if not root.left and not root.right:
                    cnt=0
                    if root.val in dic:
                        dic[root.val]+=1
                    else:
                        dic[root.val]=1
                    for i in dic:
                        if dic[i]%2!=0:
                            cnt+=1
                    if cnt<=1:
                        tot+=1
                    dic[root.val]-=1
                else:
                    if root.val in dic:
                        dic[root.val]+=1
                        func(root.left,dic)
                        func(root.right,dic)
                        dic[root.val]-=1
                    else:
                        dic[root.val]=1
                        func(root.left,dic)
                        func(root.right,dic)
                        dic[root.val]-=1
        func(root,{})
        return tot
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
