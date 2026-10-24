class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visited = set()

        def dfs(i):
            if i in visited:
                return 0
            visited.add(i)

            for j in adj[i]:
                if j == i:
                    return 0
                dfs(j)

            return 1

        res = 0
        for i in range(n):
            res += dfs(i)
        return res





