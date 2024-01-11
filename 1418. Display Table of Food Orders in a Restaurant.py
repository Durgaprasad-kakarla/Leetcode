class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        dic={}
        st=set()
        for i in orders:
            name,table,food=i
            table=int(table)
            if table in dic:
                if food not in dic[table]:
                    dic[table].update({food:1})
                else:
                    dic[table][food]+=1
            else:
                dic[table]={food:1}
            st.add(food)
        st=sorted(list(st))
        st.insert(0,'Table')
        final=[st]
        for i in sorted(dic.keys()):
            lst=[]
            lst.append(str(i))
            for j in range(1,len(st)):
                if st[j] in dic[i]:
                    lst.append(str(dic[i][st[j]]))
                else:
                    lst.append('0')
            final.append(lst)
        return final

''' Time Complexity--O(n)
    Space Complexity--O(n)'''
