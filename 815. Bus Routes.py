class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        dic={}
        maxi=0
        for i in routes:
            maxi=max(maxi,max(i))
        n=len(routes)
        for i in range(n):
            for j in routes[i]:
                if j in dic:
                    dic[j].append(i)
                else:
                    dic[j]=[i]
        queue=deque([source])
        st=set()
        steps=0
        st.add(source)
        while queue:
            count=len(queue)
            while count>0:
                node=queue.popleft()
                if node==target:
                    return steps
                for i in dic[node]:
                    for j in routes[i]:
                        if j not in st:
                            queue.append(j)
                            st.add(node)
                    routes[i]=[]
                count-=1
            steps+=1
        return -1
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
