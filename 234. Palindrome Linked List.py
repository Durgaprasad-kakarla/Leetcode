# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True
        slow,fast=head,head
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        prev.next=None
        dummy=None
        while slow:
            curr=slow.next
            slow.next=dummy
            dummy=slow
            slow=curr
        while head and dummy:
            if head.val!=dummy.val:
                return False
            head=head.next
            dummy=dummy.next
        return True
''' Time Complexity--O(n)
    Space Complexity--O(1)'''
