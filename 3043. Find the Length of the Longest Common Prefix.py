class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        st=set()
        for i in arr1:
            x=str(i)
            for j in range(len(x)):
                st.add(x[:j+1])
        n=len(arr2)
        maxi=0
        for i in range(n):
            x=str(arr2[i])
            for j in range(len(x)):
                if x[:j+1] in st:
                    maxi=max(maxi,len(x[:j+1]))
        return maxi
''' Time Complexity--O(n1+n2)
    Space Complexity--O(n1)'''
