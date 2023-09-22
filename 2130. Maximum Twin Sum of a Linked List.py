# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        dummy=ListNode(None)
        temp=head
        cnt=0
        lst=[]
        while temp:
            lst.append(temp.val)
            cnt+=1
            temp=temp.next
        maxi=0
        for i in range(cnt//2):
            maxi=max(maxi,lst[i]+lst[-(i+1)])
        return maxi
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
