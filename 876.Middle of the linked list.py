# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        count=0
        while temp is not None:
            count=count+1
            temp=temp.next
        n=count//2
        temp=head
        i=0
        while i<n:
            temp=temp.next
            i+=1
        return temp
