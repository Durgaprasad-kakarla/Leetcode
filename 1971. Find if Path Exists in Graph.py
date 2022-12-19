class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = collections.defaultdict(list)
        for a, b in edges:#appending the edges into the dictionary graph
            graph[a].append(b)
            graph[b].append(a)
        seen = [False] * n
        #We will depth first search approach
        def dfs(curr_node):
            if curr_node == destination:#if current node is destination then return True
                return True
            if not seen[curr_node]:#if it is false then it will execute
                seen[curr_node] = True
                for next_node in graph[curr_node]:
                    if dfs(next_node):
                        return True
            return False
            
        return dfs(source)
