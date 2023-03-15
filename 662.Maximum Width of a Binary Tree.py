# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def width(root):
            if not root:
                return 0
            ans=0
            queue=deque()
            queue.append([root,0])
            while queue:
                count=len(queue)
                min1=queue[0][1]
                for i in range(count):
                    x=queue.popleft()
                    cur_id=x[1]-min1
                    if i==0:
                        first=cur_id
                    if i==count-1:
                        last=cur_id
                    if x[0].left:
                        queue.append([x[0].left,cur_id*2+1])
                    if x[0].right:
                        queue.append([x[0].right,cur_id*2+2])
                ans=max(ans,last-first+1)
            return ans
        return width(root)        
