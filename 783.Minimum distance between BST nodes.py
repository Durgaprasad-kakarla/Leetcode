# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        queue=deque([root])
        list1=[]
        while  queue:
            x=queue.popleft()
            list1.append(x.val)
            if x.left:
                queue.append(x.left)
            if x.right:
                queue.append(x.right)
        list1.sort(reverse=True)
        min1=10000
        for i in range(len(list1)-1):
            if min1>list1[i]-list1[i+1]:
                min1=list1[i]-list1[i+1]
        return min1
