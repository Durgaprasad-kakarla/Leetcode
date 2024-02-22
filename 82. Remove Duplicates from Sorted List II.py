# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(None)
        head2=dummy
        last=sys.maxsize
        while head:
            if head.next:
                if head.val==head.next.val:
                    last=head.val
                if head.val!=last:
                    dummy.next=ListNode(head.val)
                    dummy=dummy.next
            else:
                if head.val!=last:
                    dummy.next=ListNode(head.val)
                    dummy=dummy.next
            head=head.next
        return head2.next
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
