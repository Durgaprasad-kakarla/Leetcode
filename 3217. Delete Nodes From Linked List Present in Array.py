# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        st=set(nums)
        temp=head
        while head.val in st:
            head=head.next
        temp=head.next
        prev=head
        while temp:
            if temp.val in st:
                prev.next=temp.next
                temp=temp.next
            else:
                prev=temp
                temp=temp.next
        return head
''' Time Complexity--O(n)
    Space Complexity--O(1)'''
