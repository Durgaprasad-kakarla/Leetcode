class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color=[-1]*len(graph)
        def check(graph,color,start):
            queue=[]
            queue.append(start)
            color[start]=0
            while queue:
                node=queue.pop(0)
                for i in graph[node]:
                    if color[i]==-1:
                        color[i]=not color[node]
                        queue.append(i)
                    elif color[i]==color[node]:
                        return False
            return True
        for i in range(len(graph)):
            if color[i]==-1:
                if check(graph,color,i)==False:
                    return False
        return True
''' Time Complexity--O(V)+O(2E)
    Space Compexity--O(V)''''
