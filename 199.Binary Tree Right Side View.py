# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def leftview(root):
            if root is None:
                return
            queue=deque([root])
            list1=[]
            while queue:
                count1=len(queue)
                for i in range(count1):
                    x=queue.popleft()
                    if i==count1-1:
                        list1.append(x.val)
                    if x.left:
                        queue.append(x.left)
                    if x.right:
                        queue.append(x.right)
            return list1
        return leftview(root)
