class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        dic={}
        for i in adjacentPairs:
            if i[0] in dic:
                dic[i[0]].append(i[1])
            else:
                dic[i[0]]=[i[1]]
            if i[1] in dic:
                dic[i[1]].append(i[0])
            else:
                dic[i[1]]=[i[0]]
        st=[]
        print(dic)
        new_dic={}
        for i in dic:
            if len(dic[i])==1:
                st.append(i)
                new_dic[i]=1
                break
        while len(st)!=len(dic):
            for i in dic[st[-1]]:
                if i in new_dic:
                    continue
                else:
                    st.append(i)
                    new_dic[i]=1
        return st
'''Time Complexity--O(n)
   Space Complexity--O(n)'''
