class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if len(matrix)*len(matrix) < k:
            return -1
        sorted_list = []
        for row in matrix:
            sorted_list.extend(row)
        sorted_list.sort()
        return sorted_list[k-1]