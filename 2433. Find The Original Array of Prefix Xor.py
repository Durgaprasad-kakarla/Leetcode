class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        n=len(pref)
        arr=[0]*len(pref)
        arr[0]=pref[0]
        for i in range(1,n):
            new=""
            for j in range(32):
                if pref[i]&(1<<j)==0:
                    if pref[i-1]&(1<<j)==0:
                        new='0'+new
                    else:
                        new='1'+new
                else:
                    if  pref[i-1]&(1<<j)==0:
                        new='1'+new
                    else:
                        new='0'+new
            arr[i]=int(new,2)
        return arr
''' Time Complexity--O(n*32)
    Space Complexity--O(n)'''
