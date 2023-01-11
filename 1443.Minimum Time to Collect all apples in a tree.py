class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
		# Return a the number of steps to reach all apples and come back
        # to the current node. Return 0 if no apples found.
        def dfs(parent, node):
            steps = 0
            for c in graph[node]:
                if c != parent:
                    steps += dfs(node, c)
            if (hasApple[node] or steps > 0) and node != 0:
                steps += 2
            return steps

        return dfs(-1, 0)
