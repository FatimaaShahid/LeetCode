from typing import List

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        y_min, y_max = m, -1
        x_min, x_max = n, -1
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    y_min = min(y_min, i)
                    y_max = max(y_max, i)
                    x_min = min(x_min, j)
                    x_max = max(x_max, j)
        

        if y_max == -1:
            return 0
        
        return (y_max - y_min + 1) * (x_max - x_min + 1)
