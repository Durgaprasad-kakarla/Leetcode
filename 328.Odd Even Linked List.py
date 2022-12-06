# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:#if nothing is there in the list then return head
            return head
        odd=head#first node as odd
        even=head.next#second node is even 
        ehead=even#it is head node for even list
        while even and even.next:#even and even.next should not be null
            odd.next=odd.next.next#connecting the odd nodes
            even.next=even.next.next#connecting the even nodes
            odd=odd.next#change the odd node to next odd node
            even=even.next#change the even node to next even node
        odd.next=ehead#finally connect the last node of odd list to the head node of the even list
        return head
