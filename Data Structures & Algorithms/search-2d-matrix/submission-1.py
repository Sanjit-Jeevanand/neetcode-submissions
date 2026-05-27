class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        m, n = len(mat), len(mat[0])
        l, r = 0, m-1
        while l <= r:
            m1 = (l+r)//2
            if mat[m1][0] <= target <= mat[m1][n-1]:
                break
            elif target < mat[m1][0]:
                r = m1 - 1
            else:
                l = m1+1
        l, r = 0, n-1
        while l <= r:
            m2 = (l+r)//2
            if mat[m1][m2] == target:
                return True
            elif mat[m1][m2] < target:
                l = m2 + 1
            else:
                r = m2 - 1
        return False