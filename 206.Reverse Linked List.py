# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        nextnode=current=head
        while nextnode is not None:
            nextnode=nextnode.next
            current.next=prev
            prev=current
            current=nextnode
        return prev
