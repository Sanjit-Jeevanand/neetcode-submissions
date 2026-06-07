class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,w in flights:
            graph[u].append((v,w))
        dq = deque([(src,0)])
        dist = [float('inf')]*n
        dist[src] = 0
        while dq and k >= 0:
            k -= 1
            lvl = len(dq)
            for _ in range(lvl):
                u,cost_u = dq.popleft()
                for v,w in graph[u]:
                    if cost_u + w < dist[v]:
                        dist[v] = cost_u + w
                        dq.append((v,dist[v]))
        return dist[dst] if dist[dst] != float('inf') else -1