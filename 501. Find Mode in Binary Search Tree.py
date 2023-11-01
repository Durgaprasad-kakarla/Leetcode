# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dic={}
        def func(root):
            if root:
                func(root.left)
                if root.val in dic:
                    dic[root.val]+=1
                else:
                    dic[root.val]=1
                func(root.right)
        func(root)
        lst=[]
        for i in dic:
            if dic[i]==max(dic.values()):
                lst.append(i)
        return lst
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
