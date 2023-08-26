# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def length(head):
            cnt = 0
            while head != None:
                cnt += 1
                head = head.next
            return cnt
        
        def dfs(left, right):
            nonlocal head
            if left > right: return None
            mid = (left + right) // 2
            leftNode = dfs(left, mid - 1)
            
            root = TreeNode(head.val)
            head = head.next
            
            root.left = leftNode
            root.right = dfs(mid + 1, right)
            return root
        
        return dfs(0, length(head)-1)
''' Time Complexity--O(
