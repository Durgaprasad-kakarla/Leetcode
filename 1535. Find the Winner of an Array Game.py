class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        cnt=0
        start=-1
        if k>=len(arr):
            return max(arr)
        while cnt!=k:
            if arr[0]<arr[1]:
                ele=arr.pop(0)
                arr.append(ele)
                if start!=-1 and start==arr[0]:
                    cnt+=1
                else:
                    start=arr[0]
                    cnt=1
            else:
                ele=arr.pop(1)
                arr.append(ele)
                if start!=-1 and start==arr[0]:
                    cnt+=1
                else:
                    start=arr[0]
                    cnt=1
        return start
''' Time Complexity--O(n)
    Space Complexity--o(1)'''
