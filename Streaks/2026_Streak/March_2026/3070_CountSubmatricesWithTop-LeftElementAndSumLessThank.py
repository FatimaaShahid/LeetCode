class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        sum_matrix = [[0]*n for _ in range(m)]
        found = 0

        for r in range(m):
            row_sum = 0
            for c in range(n):
                row_sum += grid[r][c]
                if r == 0:
                    sum_matrix [r][c] = row_sum
                else:
                    sum_matrix[r][c] = row_sum + sum_matrix[r-1][c]
                found += 1 if sum_matrix[r][c] <= k else 0
                
        return found


        