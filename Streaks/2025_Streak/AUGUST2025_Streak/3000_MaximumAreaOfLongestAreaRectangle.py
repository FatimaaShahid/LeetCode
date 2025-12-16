import math

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        longest_diagonal = 0
        max_area = 0
        
        for w, h in dimensions:
            diagonal = math.sqrt(w*w + h*h)
            area = w * h

            if diagonal > longest_diagonal or (math.isclose(diagonal, longest_diagonal) and area > max_area):
                longest_diagonal = diagonal
                max_area = area

        return max_area
