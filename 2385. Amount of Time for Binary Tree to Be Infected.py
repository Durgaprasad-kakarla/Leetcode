# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        parent_dict = {}
        stack = [(root, None)]
        while stack:
            node, parent = stack.pop()
            parent_dict[node] = parent
            if start==node.val:
                new_node=node
            if node.left:
                stack.append((node.left, node))
            if node.right:
                stack.append((node.right, node))
        queue=deque([new_node])
        dic={}
        cnt=0
        while queue:
            n=len(queue)
            for i in range(n):
                node=queue.popleft()
                dic[node]=1
                if parent_dict[node] and parent_dict[node] not in dic:
                    queue.append(parent_dict[node])
                if node.left and node.left not in dic:
                    queue.append(node.left)
                if node.right and node.right not in dic:
                    queue.append(node.right)
            cnt+=1
        return cnt-1
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
