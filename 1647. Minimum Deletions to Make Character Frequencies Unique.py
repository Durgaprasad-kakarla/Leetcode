class Solution:
    def minDeletions(self, s: str) -> int:
        dictionary=Counter(s)
        nums=sorted(list(dictionary.values()))
        st=sorted(list(set(nums)))
        lst=[]
        n=len(nums)
        x=0
        for i in range(1,max(nums)):
            if st[x]==i:
                x+=1
            else:
                lst.append(i)
        lst2=[]
        for i in range(1,n):
            if nums[i]==nums[i-1]:
                lst2.append(nums[i])
        leng=len(lst2)
        cnt=0
        for i in range(leng-1,-1,-1):
            if lst:
                while lst and lst[-1]>lst2[i]:
                    lst.pop(-1)
                if lst:
                    cnt+=(lst2[i]-lst[-1])
                    lst.pop(-1)
                else:
                    cnt+=(lst2[i])
            else:
                cnt+=lst2[i]
        return cnt
''' Time Complexity--O(nlogn)
    Space Complexity--O(n)'''
