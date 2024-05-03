class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1=version1.split(".")
        version2=version2.split(".")
        n1=len(version1)
        n2=len(version2)
        def func(st):
            if int(st)!=0:
                return str(int(st))
            return st
        def func2(st):
            n=len(st)
            for i in range(n-1,-1,-1):  
                if int(st[i])==0:
                    st[i]=''
                else:
                    break
            return "".join(st)
        for i in range(min(n1,n2)):
            st1=func(version1[i])
            st2=func(version2[i])
            if int(st1)<int(st2):
                return -1
            elif int(st1)>int(st2):
                return 1
            else:
                version1[i]=st1
                version2[i]=st2
        st1=func2(version1)
        st2=func2(version2)
        if st1>st2:
            return 1
        elif st1<st2:
            return -1
        return 0
''' Time Complexity--O(min(n1,n2))
    Space Complexity--O(1)'''
