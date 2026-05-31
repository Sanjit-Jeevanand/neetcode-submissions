class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        def nq(i,curr,d1,d2):
            if len(curr) == n:
                curr3 = []
                for i in curr:
                    curr2 = ["."]*n
                    curr2[i] = "Q"
                    curr3.append("".join(curr2.copy()))
                ans.append(curr3.copy())
                return
            for j in range(n):
                if j not in curr and i+j not in d1 and i-j not in d2:
                    curr.append(j)
                    d1.add(i+j)
                    d2.add(i-j)
                    nq(i+1,curr,d1,d2)
                    curr.pop()
                    d1.remove(i+j)
                    d2.remove(i-j)
        nq(0,[],set(),set())
        return ans