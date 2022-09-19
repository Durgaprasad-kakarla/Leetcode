# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        prev=head
        temp=prev.next
        while temp is not None:
            if prev.val==temp.val:
                prev.next=temp.next
                temp=temp.next
            else:
                prev=temp
                temp=temp.next
        return head
