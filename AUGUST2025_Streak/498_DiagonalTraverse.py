
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []

        m, n = len(mat), len(mat[0])
        ans = []
        i, j = 0, 0
        direction = 1  

        for _ in range(m * n):
            ans.append(mat[i][j])

            if direction == 1:  
                if j == n - 1:  
                    i += 1
                    direction = -1
                elif i == 0:  
                    j += 1
                    direction = -1
                else:  
                    i -= 1
                    j += 1
            else:  
                if i == m - 1:  
                    j += 1
                    direction = 1
                elif j == 0:  
                    i += 1
                    direction = 1
                else:  
                    i += 1
                    j -= 1

        return ans
