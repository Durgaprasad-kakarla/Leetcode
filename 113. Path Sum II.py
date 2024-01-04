# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans=[]
        def func(root,target,lst):
            if root:
                if not root.left and not root.right:
                    if target==root.val:
                        lst+=[root.val]
                        ans.append(lst)
                        return 
                    else:
                        return 
                else:
                    func(root.left,target-root.val,lst+[root.val])
                    func(root.right,target-root.val,lst+[root.val])
        func(root,targetSum,[])
        return ans

''' Time Complexity--O(n)
    Space Complexity--O(h*x)-->x--no.of possible lists and h is height'''
