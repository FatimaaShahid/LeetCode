class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        special = 0

        for r in range(m):
            for c in range(n):
                if mat[r][c] == 1 and sum(mat[r])==1:
                    cnt = 0
                    for i in range(m):
                        cnt += mat[i][c]
                        if cnt>1:
                            break
                    if cnt == 1:
                        special += 1
        return special



        