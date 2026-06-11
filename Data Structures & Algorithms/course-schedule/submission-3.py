class Solution:
    def canFinish(self, n: int, prereq: List[List[int]]) -> bool:
        graph = defaultdict(list)
        pq = [0]*n
        dq = deque()
        for i,j in prereq:
            graph[j].append(i)
            pq[i] += 1
        for i in range(n):
            if pq[i] == 0:
                dq.append(i)
        if not dq: return False
        while dq:
            x = dq.popleft()
            for i in graph[x]:
                pq[i] -= 1
                if pq[i] == 0:
                    dq.append(i)
        return all(x == 0 for x in pq)
