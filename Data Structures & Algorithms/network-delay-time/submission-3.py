class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))
        h = [(0,k)]
        ans = [float('inf')]*(n+1)
        ans[k] = 0
        while h:
            cost_u, u = heapq.heappop(h)
            for v,w in graph[u]:
                if w+cost_u < ans[v]:
                    ans[v] = w+cost_u
                    heapq.heappush(h,(ans[v],v))
        if any(x == float('inf') for x in ans[1:]):
            return -1
        return max(ans[1:])