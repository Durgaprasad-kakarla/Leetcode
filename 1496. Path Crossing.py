class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x,y=0,0
        st=set()
        st.add((0,0))
        for i in path:
            print(st)
            if i=='N':
                x,y=x-1,y
            elif i=='E':
                x,y=x,y+1
            elif i=='S':
                x,y=x+1,y
            else:
                x,y=x,y-1
            if (x,y) in st:
                return True
            st.add((x,y))
        return False
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
