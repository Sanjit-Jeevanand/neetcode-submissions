class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x,y):
            x,y = find(x),find(y)
            if y != x:
                parent[y] = x
            return
        n = len(edges)
        parent = [i for i in range(n+1)]
        for i,j in edges:
            if find(i) == find(j):
                return [i,j]
            union(i,j)