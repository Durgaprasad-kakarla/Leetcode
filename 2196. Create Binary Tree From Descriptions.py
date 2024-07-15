# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        dic={}
        tot_children=set()
        child_dic={}
        for parent,child,isleft in descriptions:
            if parent in dic:
                if child in dic:
                    if isleft:
                        dic[parent].left=dic[child]
                    else:
                        dic[parent].right=dic[child]
                else:
                    newchildren=TreeNode(child)
                    if isleft:
                        dic[parent].left=newchildren
                    else:
                        dic[parent].right=newchildren
                    dic[child]=newchildren
            else:
                if parent not in dic:
                    newnode=TreeNode(parent)
                    dic[parent]=newnode

                if child in dic:
                    if isleft:
                        dic[parent].left=dic[child]
                    else:
                        dic[parent].right=dic[child]
                else:
                    newchildren=TreeNode(child)
                    if isleft:
                        dic[parent].left=newchildren
                    else:
                        dic[parent].right=newchildren
                    dic[child]=newchildren
            tot_children.add(child)
        for i in dic:
            if i not in tot_children:
                return dic[i]
        
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
