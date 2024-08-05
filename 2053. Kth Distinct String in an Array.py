class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dic=Counter(arr)
        cnt=0
        for i in arr:
            if dic[i]==1:
                cnt+=1
                if cnt==k:
                    return i
        return ''
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
