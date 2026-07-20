class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        
        oned = []
        for row in grid:
            oned.extend(row)
        k %= len(oned)
        print(oned)
        oned = oned[-k:] + oned[:-k]
        print(oned)

        new = []
        idx = 0
        for _ in range(m):
            new.append(oned[idx:idx+n])
            idx+=n
        return new


        