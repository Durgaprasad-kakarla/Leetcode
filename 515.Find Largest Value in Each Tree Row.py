# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        def largest(root):
            if root is None:
                return 
            queue=deque([root])
            list1=[]
            while queue:
                count1=len(queue)
                max1=sys.maxsize*-1#It is used to find very small integer value
                for i in range(count1):
                    x=queue.popleft()
                    if max1<x.val:
                        max1=x.val
                    if x.right:
                        queue.append(x.right)
                    if x.left:
                        queue.append(x.left)
                list1.append(max1)
            return list1
        return largest(root)
