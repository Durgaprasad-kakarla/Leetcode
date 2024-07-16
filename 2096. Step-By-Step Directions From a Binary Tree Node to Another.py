# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def lca(node): 
            if not node or node.val in (startValue , destValue): 
                return node 
            left, right = lca(node.left), lca(node.right)
            if left and right:
                return node
            else:
                return left or right
        node=lca(root)
        queue=deque()
        queue.append([node,''])
        path_start,path_dest='',''
        while queue:
            node,s=queue.popleft()
            if node.val==startValue:
                path_start=s
            if node.val==destValue:
                path_dest=s
            if node.left:
                queue.append([node.left,s+'L'])
            if node.right:
                queue.append([node.right,s+'R'])
        return 'U'*(len(path_start))+path_dest
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
