class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        st=set()
        for i in paths:
            st.add(i[0])
        for i in paths:
            if i[1] not in st:
                return i[1]
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
