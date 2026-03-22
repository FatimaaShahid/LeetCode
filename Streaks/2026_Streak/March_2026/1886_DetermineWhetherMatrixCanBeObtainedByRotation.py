
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        
        def rotate(matrix):
            n = len(matrix)
            new = []
            for j in range(n):
                new_row = []
                for i in range(n):
                    new_row.append(matrix[i][j])
                new_row.reverse()
                new.append(new_row)
            return new

        for _ in range(4):
            if mat == target:
                return True
            mat = rotate(mat)

        return False