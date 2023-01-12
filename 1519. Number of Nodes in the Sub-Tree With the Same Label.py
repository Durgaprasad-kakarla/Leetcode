class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        tree = defaultdict(list)
        for s,e in edges:
            tree[s].append(e)
            tree[e].append(s)
        print(tree)
        res = [0] * n
        def dfs(node, par):
            nonlocal res
            # Since there are at most 26 lowercase English letters 
            count = Counter()
            for nei in tree[node]:
                # Make sure we are not going backward to its parent node.
                if nei != par:
                    # Update count with the letters' frequency in the children nodes
                    # This is the same as going through a to z and increase the frequency of each letter.
                    count += dfs(nei, node)
            
            count[labels[node]] += 1
            res[node] = count[labels[node]]
            
            return count
        
        # Starting from node 0, and assign fake parent -1 for it.
        dfs(0,-1)
        return res
