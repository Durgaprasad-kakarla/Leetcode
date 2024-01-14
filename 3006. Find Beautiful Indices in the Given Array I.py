class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        lst=[]
        n=len(s)
        len_a=len(a)
        len_b=len(b)
        for i in range(n):
            if s[i:i+len_a]==a:
                lst.append(i)
        lst2=[]
        for i in range(n):
            if s[i:i+len_b]==b:
                lst2.append(i)
        final=[]
        def binary_search(arr,ele,k):
            l,r=0,len(arr)-1
            while l<=r:
                mid=(l+r)//2
                if arr[mid]<=ele:
                    if abs(arr[mid]-ele)<=k:
                        return True
                    l=mid+1
                else:
                    if abs(arr[mid]-ele)<=k:
                        return True
                    r=mid-1
            return False
        for i in lst:
            if binary_search(lst2,i,k):
                final.append(i)
        return final
''' Time Complexity--O(n+(nlogn)
    Space Complexity--O(n)
