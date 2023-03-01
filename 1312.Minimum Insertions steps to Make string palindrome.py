class Solution:
    def minInsertions(self, s: str) -> int:
        s1=s
        s2=s1[::-1]
        prev=[0 for j in range(len(s2)+1)]
        for ind1 in range(1,len(s1)+1):
            cur=[0 for j in range(len(s2)+1)]
            for ind2 in range(1,len(s2)+1):
                if s1[ind1-1]==s2[ind2-1]:
                    cur[ind2]=1+prev[ind2-1]
                else:
                    cur[ind2]=max(prev[ind2],cur[ind2-1])
            prev=cur
            print(prev)
        return len(s1)-prev[len(s1)]
