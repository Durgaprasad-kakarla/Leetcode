# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow,fast=head,head
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        if fast is None:
            head2=slow
            prev.next=None
        else:
            head2=slow.next
            slow.next=None
        dummy=None
        while head2:
            curr=head2.next
            head2.next=dummy
            dummy=head2
            head2=curr
        temp=head
        while temp and dummy:
                curr=temp.next
                curr2=dummy.next
                temp.next=dummy
                dummy.next=curr
                temp=curr
                dummy=curr2
''' Time Complexity--O(n)
    Space Complexity--O(n//2)'''
