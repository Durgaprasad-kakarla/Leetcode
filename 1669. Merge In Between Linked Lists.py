# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        temp2=list2
        while temp2.next:
            temp2=temp2.next
        temp1=list1
        cnt=0
        while temp1:
            cnt+=1
            if cnt==a:
                start=temp1
            if cnt==b+1:
                start.next=list2
                temp2.next=temp1.next
                return list1
            temp1=temp1.next
''' Time Complexity--O(n1+n2)
    Space Complexity--O(1)'''
