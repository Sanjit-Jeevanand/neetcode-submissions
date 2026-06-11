class Solution:
    def findOrder(self, n: int, prereq: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        pq = [0]*n
        dq = deque()
        ans = []
        for i,j in prereq:
            graph[j].append(i)
            pq[i] += 1
        for i in range(n):
            if pq[i] == 0:
                dq.append(i)
                ans.append(i)
        while dq:
            x = dq.popleft()
            for i in graph[x]:
                pq[i] -= 1
                if pq[i] == 0:
                    ans.append(i)
                    dq.append(i)
        return ans if all(x == 0 for x in pq) else []