class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        adj_lst=defaultdict(list)
        for u,v in edges:
            adj_lst[u].append(v)
            adj_lst[v].append(u)
        queue=deque([1])
        cur_time=0
        res=-1
        visit_times=defaultdict(list)
        while queue:
            for i in range(len(queue)):
                node=queue.popleft()
                if node==n:
                    if res!=-1:
                        return cur_time
                    res=cur_time
                for adj in adj_lst[node]:
                    times=visit_times[adj]
                    if len(times)==0 or (len(times)==1 and times[0]!=cur_time):
                        queue.append(adj)
                        times.append(cur_time)
            if (cur_time//change)&1==1:
                cur_time+=(change-cur_time%change)
            cur_time+=time
        return -1
''' Time Complexity--O(2*(V+E))  
    Space Complexity--O(V)'''
