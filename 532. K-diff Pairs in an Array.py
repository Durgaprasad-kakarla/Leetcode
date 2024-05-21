class Solution:
    def findPairs(self, arr: List[int], x: int) -> int:
        dic={}
        n=len(arr)
        for i in range(n):
            if arr[i] not in dic:
                dic[arr[i]]=1
            else:
                dic[arr[i]]+=1
        if x==0:
            cnt=0
            for i in dic:
                if dic[i]>1:
                    cnt+=1
            return cnt
        cnt=0
        st=set()
        for i in range(n):
            if arr[i]+x in dic and (arr[i],arr[i]+x) not in st:
                cnt+=1
                st.add((arr[i],arr[i]+x))
        return cnt
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
