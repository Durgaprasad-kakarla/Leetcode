class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topological_sort(edges,k):
            adj=[[] for i in range(k)]
            indegree=[0]*(k+1)
            for u,v in edges:
                adj[u-1].append(v-1)
                indegree[v-1]+=1
            queue=deque()
            for i in range(k):
                if indegree[i]==0:
                    queue.append(i)
            topo={}
            cnt=0
            while queue:
                node=queue.popleft()
                topo[node]=cnt
                for i in adj[node]:
                    indegree[i]-=1
                    if indegree[i]==0:
                        queue.append(i)
                cnt+=1
            if len(topo)==k:
                return topo
            return -1
        rows=(topological_sort(rowConditions,k))
        cols=(topological_sort(colConditions,k))
        # print(rows,cols)
        if rows==-1 or cols==-1:
            return []
        mat=[[0 for i in range(k)] for j in range(k)]
        for row,ind in sorted(rows.items(),key=lambda x:x[1]):
            print(row+1)
            mat[ind][cols[row]]=row+1
        return mat
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
