# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        while head:
            arr.append(head.val)
            head=head.next
        def find_consecutive(arr):
            dic={}
            n=len(arr)
            pref=0
            lst=[]
            for i in range(n):
                pref+=arr[i]
                if pref==0:
                    return [0,i]
                if pref in dic:
                    return [dic[pref]+1,i]
                dic[pref]=i
            return []
        while True:
            lst=find_consecutive(arr)
            if lst!=[]:
                x=lst[0]
                y=lst[1]
                for i in range(x,y+1):
                    arr[i]=float('inf')
                l=[]
                for i in range(len(arr)):
                    if arr[i]!=float('inf'):
                        l.append(arr[i])
                arr=l.copy()
            else:
                break
            
        dummy=ListNode(None)
        temp=dummy
        n=len(arr)
        for i in range(n):
            if arr[i]!=float('inf'):
                temp.next=ListNode(arr[i])
                temp=temp.next
        return dummy.next

''' Time Complexity--O(n^2)
    Space Complexity--O(n)'''
