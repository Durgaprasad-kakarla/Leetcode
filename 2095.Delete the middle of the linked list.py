# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        count=0
        while temp is not None:
            count=count+1
            temp=temp.next
        if count==1:
            return None
        n=count//2+1
        temp=head
        prev=head
        i=0
        while i<n-1:
            prev=temp
            temp=temp.next
            i+=1
        prev.next=temp.next
        return head
