class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count1=0
        for i in range(len(strs[0])):
            st=''
            for s in strs:
                st=st+s[i]
            if sorted(st)!=list(st):
                count1+=1
        return count1
