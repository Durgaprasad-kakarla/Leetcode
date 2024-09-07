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
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def func(root,temp,head):
            if not temp:
                return True
            if not root:
                return False
            if temp!=head and temp.val!=root.val:
                return False
            if temp==head and head.val==root.val:
                if func(root.left,head.next,head) or func(root.right,head.next,head):
                    return True
                if func(root.left,temp,head) or func(root.right,temp,head):
                    return True
            elif temp!=head and temp.val==root.val:
                if func(root.left,temp.next,head) or func(root.right,temp.next,head):
                    return True
            else:
                if func(root.left,temp,head) or func(root.right,temp,head):
                    return True
            return False
        return func(root,head,head)
''' Time Complexity--O(n*m)
    Space Complexity--O(n)'''
