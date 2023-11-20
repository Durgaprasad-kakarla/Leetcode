class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        truck=['P','M','G']
        st="".join(garbage)
        cnt=0
        for i in range(3):
            for j in range(len(garbage)-1,-1,-1):
                if truck[i] in garbage[j]:
                    if j==0:
                        cnt+=st.count(truck[i])
                    else:
                        cnt+=st.count(truck[i])+sum(travel[:j])
                    break
        return cnt
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
