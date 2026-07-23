class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]


        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # [[1], [0, 2], [1], [4], [3]]

        count = 0

        visited = [False] * n

        def dfs(v,visited):
            visited[v] = True
            for neighbor in graph[v]:
                if visited[neighbor] == False:
                    dfs(neighbor,visited)

        for v in range(n):
            if visited[v] == False:
                dfs(v,visited)
                count+=1


        return count

        